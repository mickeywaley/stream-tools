import base64
import datetime
import os
import subprocess
import threading
import time
import traceback
import urllib
from pathlib import Path

import requests
from Crypto.Cipher import AES

from playlist.crawler.common.url_crawler import UrlCrawler


class ThumbDownloadThread(threading.Thread):
    def __init__(self, id,  url, download_path, mongo):
        threading.Thread.__init__(self)
        self.id = id
        self.url = url
        self.download_path = download_path
        self.key = None

        self.mongo = mongo

    def run(self):

        download_path = self.download_path

        if not os.path.exists(download_path):
            os.mkdir(download_path)

        all_content = UrlCrawler.curl(self.url)

        print(all_content)

        file_line = all_content.splitlines()

        if not file_line or len(file_line) == 0:
            self.index_thumb(self.id, self.url, '')
            raise BaseException(u"获取M3U8失败")
        # 通过判断文件头来确定是否是M3U8文件
        if file_line[0] != "#EXTM3U":
            raise BaseException(u"非M3U8的链接")

        for index, line in enumerate(file_line):
            if "EXTINF" in line or "EXT-X-STREAM-INF" in line:
                # 拼出ts片段的URL
                pd_url = file_line[index + 1]

                inner_url = self.get_inner_url(self.url, pd_url)

                print(inner_url)

                if pd_url.find('.ts') > 0:
                    ret, path = self.download_ts_file(self.url, inner_url, download_path, self.key)

                    if ret:
                        print("[OK]: id:{}, url {}, path {}".format(self.id, self.url, path))
                        self.index_thumb(self.id, self.url, path)


                else:
                    ThumbDownloadThread(self.id, inner_url, download_path, self.mongo).start()

                break

    def index_thumb(self, id, url, path):

        try:
            print("{}[Index-Thumb]: {}".format(id, url))

            if path:
                file_name = Path(path).name

            myquery = {"_id": id}

            doc = {
                "thumb_time": time.mktime(datetime.datetime.now().timetuple()),
                "thumb": file_name
            }
            self.mongo.db.playitems.update_one(myquery, {'$set': doc}, upsert=True)
        except Exception as ex:
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
    def download_ts_file(m3u8, ts_url, download_dir, key):

        file_name = ts_url[ts_url.rfind('/'):]
        print('[file_name]:', file_name)
        curr_path = '%s%s' % (download_dir, file_name)

        thumb_name = bytes.decode(base64.b64encode(m3u8.encode(encoding="UTF-8")))

        thumb_path = os.path.join(download_dir, '%s.jpg' % (thumb_name))
        print('[download]:', ts_url)
        print('[target]:', curr_path)
        if os.path.isfile(curr_path):
            print('[warn]: file already exist')
            return True, curr_path
        try:
            res = requests.get(ts_url)
            with open(curr_path, 'ab') as f:
                if key and len(key): # AES 解密
                    cryptor = AES.new(key, AES.MODE_CBC, key)
                    f.write(cryptor.decrypt(res.content))
                else:
                    f.write(res.content)

                f.flush()
            print('[OK]: {} saved'.format(curr_path))

            print("thumb path:{}".format(thumb_path))

            command = [ 'ffmpeg',
                        '-y',
                        '-i', curr_path,
                        '-ss', '00:00:01.000',
                        '-vframes', '1',
                        thumb_path
                        ]

            process = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

            (stdoutdata, stderrdata) = process.communicate()

            print(stdoutdata)

            print(stderrdata)

            os.remove(curr_path)
            if os.path.exists(thumb_path) and os.path.getsize(thumb_path) > 0:

                return True, thumb_path
            else:

                return False, None
        except Exception as es:
            print('[warn]: download error:{}'.format(ts_url))
            print('[warn]: {} deleted'.format(curr_path))
            print(es)
            traceback.print_stack()
            os.remove(curr_path)

            return False, None