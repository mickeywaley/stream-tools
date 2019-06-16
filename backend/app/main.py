import datetime
import json
import os
import subprocess
import time
import urllib
from urllib.parse import urlparse

from bson import ObjectId
from flask import Flask, jsonify, request
# from flask_restful import Resource, Api
from flask_pymongo import PyMongo

from flask_apscheduler import APScheduler

from common import JSONEncoder
from thumb_download_thread import ThumbIndexJob

from config import Config

app = Flask(__name__)
# api = Api(app)

app.config['MONGO_DBNAME'] = Config.MONGO_DBNAME
app.config['MONGO_URI'] = Config.MONGO_URI


app.config['JOBS'] = [
    {
        'id': 'thumb_index_job',
        'func': 'main:thumb_index_job',
        'trigger': 'interval',
        'seconds': 3
    }
]

app.config['SCHEDULER_API_ENABLED'] = True

mongo = PyMongo(app)

filepath = os.path.abspath(__file__)

thumb_path = os.path.join(os.path.dirname(filepath), "../../nginx/dist/images/thumbs")


def thumb_update_job():

    result = mongo.db.playitems.find({})
    for s in result:

        myquery = {"_id": s['_id']}

        try:
            thumb_success = len(s['thumb']) > 0
        except:

            thumb_success = False



        doc = {
            "thumb_success": thumb_success
        }
        mongo.db.playitems.update_one(myquery, {'$set': doc}, upsert=True)

        print(s['_id'])





def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

@app.route('/playitems')
def playitems():
    channel = request.args.get('channel')
    keyword = request.args.get('keyword')

    page_num = 1 if not request.args.get('pageNum') or not is_number(request.args.get('pageNum')) or int(request.args.get('pageNum')) < 1 else int(request.args.get('pageNum'))

    page_size = 20 if not request.args.get('pageSize') or not is_number(request.args.get('pageSize')) else int(request.args.get('pageSize'))

    skip = (page_num - 1)*page_size

    query = []
    if channel:
        channel_query = {"channel": {"$eq": channel}}
        query.append(channel_query)
    if keyword:
        keyword_query = {"tags": {"$elemMatch": {"$regex": ".*{}.*".format(keyword), "$options": "i"}}}
        query.append(keyword_query)

    if len(query) > 0:
        result = mongo.db.playitems.find({"$and": query}).sort([("thumb_success", -1), ("thumb_time", -1)])
    else:
        result = mongo.db.playitems.find().sort([("thumb_success", -1), ("thumb_time", -1)])

    count = result.count()

    print(count)

    result = result.skip(skip).limit(page_size)

    output = []
    for s in result:
        output.append(s)

    return JSONEncoder().encode({
        "pagination": {
            "current_page": page_num,
            "total_count": count,
            "page_size": page_size
        },
        "data": output
    })


@app.route('/channels')
def channels():

    channel = request.args.get('channel')
    keyword = request.args.get('keyword')
    type = request.args.get('type')

    page_num = 1 if not request.args.get('pageNum') or not is_number(request.args.get('pageNum')) or int(request.args.get('pageNum')) < 1 else int(request.args.get('pageNum'))

    page_size = 20 if not request.args.get('pageSize') or not is_number(request.args.get('pageSize')) else int(request.args.get('pageSize'))

    skip = (page_num - 1)*page_size

    query = []
    if channel:
        channel_query = {"_id": {"$eq": channel}}
        query.append(channel_query)
    if keyword:
        keyword_query = {"name": {"$regex": ".*{}.*".format(keyword), "$options": "i"}}
        query.append(keyword_query)
    if type:
        type_query = {"type": {"$eq": type}}
        query.append(type_query)

    result = []
    if len(query) > 0:
        result = mongo.db.channels.find({"$and": query})

    else:
        result = mongo.db.channels.find()

    count = result.count()

    print(count)

    result = result.skip(skip).limit(page_size)

    output = []
    for s in result:
        output.append(s)

    return JSONEncoder().encode({
        "pagination": {
            "current_page": page_num,
            "total_count": count,
            "page_size": page_size
        },
        "data": output
    })


if __name__ == '__main__':

    # url = 'http://223.110.241.203:6610/gitv/live1/G_JINYING/G_JINYING/c001_1560676598_1560676608.ts?ts_min=1&zte_auth=6201d93d&zduration=10&srcurl=aHR0cDovLzExMi4yNS43LjEyOS9naXR2X2xpdmUvR19KSU5ZSU5H';
    # o = urlparse(url)
    #
    # print(o.path)

    # curr_path = '/Users/zhiyongli/Programs/github/stream-tools/backend/app/../../nginx/dist/images/thumbs/1560675985-1-1530921057.hls.ts'
    #
    # file_name = curr_path[curr_path.rfind('/') + 1:] + ".jpeg"
    # print('[file_name]:', file_name)
    #
    # print('[thumb_path]:', thumb_path)
    #
    #
    # thumb_jpeg_path = os.path.join(thumb_path, file_name)
    #
    # print('[thumb_jpeg_path]:', thumb_jpeg_path)
    #
    # ## ffmpeg -v -ss '00:00:01.000' -vframes 1 -i
    # command = ['ffmpeg',
    #            '-y',
    #            '-v', 'error',
    #            '-i', curr_path,
    #            '-ss', '00:00:01.000',
    #            '-vframes', '1',
    #            thumb_jpeg_path
    #            ]
    #
    # process = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    #
    # (stdoutdata, stderrdata) = process.communicate()
    #
    # print(stdoutdata)
    #
    # print(stderrdata)
    # thumb_jpeg_path = os.path.join(thumb_path, '2c7815b9567c2de428983ef1dd11ca95.jpg')
    #
    # try:
    #     command = ['ffprobe',
    #                '-v', 'error',
    #                '-select_streams', 'v:0',
    #                '-show_entries', 'stream=width,height',
    #                '-of', 'csv=s=x:p=0',
    #                thumb_jpeg_path
    #                ]
    #
    #     process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    #
    #     (stdoutdata, stderrdata) = process.communicate()
    #
    #     print('[FFMPROB]:{}{}'.format(stdoutdata, stderrdata))
    #
    #     if stdoutdata and len(stdoutdata) > 0:
    #         thumb_resolution = stdoutdata.decode('utf-8').strip()
    #         print("[thumb_resolution]:{}-{}".format(thumb_resolution, thumb_jpeg_path))
    #
    #
    # except:
    #     pass



    ThumbIndexJob(thumb_path, mongo).start()

    app.debug = True

    app.run()
