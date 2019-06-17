import datetime
import hashlib
import os
import queue
import subprocess
import threading
import time
import traceback
from pathlib import Path
from queue import Queue
from urllib.parse import urlparse

import requests

from common import JSONEncoder
from config import Config


class ThumbIndexJob(threading.Thread):

    def __init__(self, thumb_path, mongo):
        threading.Thread.__init__(self)
        self.thumb_path = thumb_path
        self.mongo = mongo
        self.queue = Queue(Config.THUMB_WORKDER_COUNT)
        self.running_job = True
        print(' {} inited...............'.format(self.ident))

    def run(self):

        if not os.path.exists(self.thumb_path):
            os.makedirs(self.thumb_path)

        for i in range(0, Config.THUMB_WORKDER_COUNT):
            ThumbDownloadWorker(self.queue, self.thumb_path, self.mongo).start()

        print(' {} worker started...............'.format(self.ident))

        full_count = 0

        while self.running_job:

            if self.queue.full():
                print('queue full:{}, {}- {}'.format(self.queue.qsize(),self.queue.maxsize, full_count))
                time.sleep(3)
                full_count += 1
                continue


            full_count = 0
            try:

                interval_time = time.mktime(datetime.datetime.now().timetuple()) - 60*60*2

                result = self.mongo.db.playitems.find({"thumb_time": {"$lt": interval_time}}).sort([("thumb_success", -1), ("thumb_time", -1)])

                print('{} running: {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), result.count()))


                if result.count() == 0:

                    time.sleep(60)
                else:

                    for s in result:
                        print(JSONEncoder().encode(s))
                        # output.append(s)
                        self.queue.put([s['_id'], s['url']], block=True, timeout=None)

                        print('now running:{}'.format(self.queue.qsize()))

            except Exception as ex:
                traceback.print_exc()
                print('queue except:{}, {}'.format(self.queue.qsize(), self.queue.maxsize))
                pass


class ThumbDownloadWorker(threading.Thread):
    def __init__(self, queue, download_path, mongo):
        threading.Thread.__init__(self)
        self.queue = queue
        self.download_path = download_path
        self.mongo = mongo
        self.thread_stop = False

    def run(self):

        while not self.thread_stop:

            try:
                task=self.queue.get(block=True, timeout=10)#接收消息

                print("\n\n----------------------------------------------")

                print("task recv:%s ,task url:%s" % (task[0], task[1]))

                self.dowload_and_index(task[0], task[1])

                self.queue.task_done()

            except queue.Empty:
                print("thread[%d] %s: waiting for task" %(self.ident, self.name))
                time.sleep(3)
            except Exception as ex:
                print("thread[%d] %s: exception for task" %(self.ident, self.name))
                pass


    def dowload_and_index(self, id, url):

        print("[Thread] start:{}".format(url))

        download_path = self.download_path

        try:

            all_content = requests.get(url, timeout=1).text
        except:

            self.index_thumb(id, url, path='')
            return

        # print("all_content:" + all_content)

        file_line = all_content.splitlines()

        if not file_line or len(file_line) == 0:
            self.index_thumb(id, url, path='')
            raise BaseException(u"获取M3U8失败")
        # 通过判断文件头来确定是否是M3U8文件
        if file_line[0] != "#EXTM3U":
            self.index_thumb(id, url, delete=True, path='')
            raise BaseException(u"非M3U8的链接")

        for index, line in enumerate(file_line):
            if "EXTINF" in line or "EXT-X-STREAM-INF" in line:
                # 拼出ts片段的URL
                pd_url = file_line[index + 1]

                inner_url = self.get_inner_url(url, pd_url)

                print(inner_url)

                if pd_url.find('.ts') > 0:
                    ret, path, resolution = self.download_ts_file(url, inner_url, download_path)

                    if ret:
                        print("[OK-TS]: id:{}, url {}, path {}, resolution:{}".format(id, url, path, resolution))
                        self.index_thumb(id, url, path=path, resolution=resolution)
                    else:

                        print("[ERROR-TS]: id:{}, url {}, path {}".format(id, url, path))
                        self.index_thumb(id, url)

                else:
                    self.queue.put([id, inner_url], block=True, timeout=None)

                break

    def index_thumb(self, id, url, delete=False, path=None, resolution=None):
        print("[Index-Thumb]{}: {}".format(id, url))
        try:
            myquery = {"url": url}
            #
            # if delete:
            #     self.mongo.db.playitems.delete_one(myquery)
            #     return

            if path:
                file_name = Path(path).name
            else:
                file_name = ''

            thumb_resolution = ''

            if resolution:

                thumb_resolution = resolution

            if len(file_name) > 0:

                doc = {
                    "thumb_time": time.mktime(datetime.datetime.now().timetuple()),
                    "thumb": file_name,
                    "thumb_success": len(file_name) > 0,
                    "thumb_resolution": thumb_resolution,
                    "thumb_failed_count": 0

                }

                updateQuery = {'$set': doc}

                print("[OK-MONGO]:{}".format(id))

                result = self.mongo.db.playitems.update_one(myquery, updateQuery, upsert=True)

                print("[UPDATE-MONGO:matched-{}, modified-{}]".format(result.matched_count, result.modified_count))


            else:
                doc = {
                    "thumb_time": time.mktime(datetime.datetime.now().timetuple()),
                    "thumb": file_name,
                    "thumb_success": len(file_name) > 0,
                    "thumb_resolution": thumb_resolution,

                }
                updateQuery = {'$set': doc, '$inc': {"thumb_failed_count": 1}}

                self.mongo.db.playitems.update_one(myquery, updateQuery, upsert=True)

        except Exception as ex:
            traceback.print_exc()
            print("index_thumb {} error for url :{}".format(id, url))
            pass

    @staticmethod
    def get_inner_url(url, path):

        base_url = url.rsplit('/', 1)[0]

        if path.startswith('http'):
            return path
        else:
            return '%s/%s' % (base_url, path)

    @staticmethod
    def md5_filepath(filepath):

        hl = hashlib.md5()
        hl.update(filepath.encode(encoding='utf-8'))

        return hl.hexdigest()



    @staticmethod
    def download_ts_file(m3u8, ts_url, download_dir):

        o = urlparse(ts_url)

        # print(o.path)

        file_name = o.path[o.path.rfind('/'):]
        print('[file_name]:', file_name)
        curr_path = '%s%s' % (download_dir, file_name)

        thumb_name = ThumbDownloadWorker.md5_filepath(m3u8)

        thumb_path = os.path.join(download_dir, '%s.jpg' % (thumb_name))
        print('[download]:', ts_url)
        print('[target]:', curr_path)
        # if os.path.isfile(curr_path):
        #     print('[warn]: file already exist')
        #     return True, curr_path
        try:
            res = requests.get(ts_url)

            if res.status_code != 200:

                return False, None, None

            with open(curr_path, 'ab') as f:
                # if key and len(key): # AES 解密
                #     cryptor = AES.new(key, AES.MODE_CBC, key)
                #     f.write(cryptor.decrypt(res.content))
                # else:
                f.write(res.content)

                f.flush()
            # print('[OK]: {} saved'.format(curr_path))

            print("[thumb]ts:{},thumb path:{}".format(curr_path, thumb_path))


            ## ffmpeg -v -ss '00:00:01.000' -vframes 1 -i
            command = ['ffmpeg',
                       '-y',
                       '-v', 'error',
                       '-i', curr_path,
                       '-ss', '00:00:01.000',
                       # '-vf', 'scale="256:192"'
                       '-vframes', '1',
                       thumb_path
                       ]

            process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            (stdoutdata, stderrdata) = process.communicate()


            print('[FFMPEG]:{}{}'.format(stdoutdata, stderrdata))


            thumb_resolution = None

            if os.path.exists(thumb_path) and os.path.getsize(thumb_path) > 0:
                print("[Success]:{}".format(curr_path))

                os.remove(curr_path)
                #ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0

                try:
                    command = ['ffprobe',
                               '-v', 'error',
                               '-select_streams', 'v:0',
                               '-show_entries', 'stream=width,height',
                               '-of', 'csv=s=x:p=0',
                               thumb_path
                               ]

                    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                    (stdoutdata, stderrdata) = process.communicate()

                    print('[FFMPROB]:{}{}'.format(stdoutdata, stderrdata))

                    if stdoutdata and len(stdoutdata) > 0:
                        print("[thumb_resolution]:{}-{}".format(stdoutdata, curr_path))

                        thumb_resolution = stdoutdata.decode('utf-8').strip()
                except:
                    pass

                return True, thumb_path, thumb_resolution
            else:
                print("[Failed]:{}".format(curr_path))
                return False, None, None

        except Exception as es:
            print('[warn]: download error:{}'.format(ts_url))
            print('[warn]: {} deleted'.format(curr_path))
            print(es)
            traceback.print_stack()
            try:
                os.remove(curr_path)
            except:
                pass

            return False, None, None