import datetime
import json
import os
import time

from bson import ObjectId
from flask import Flask, jsonify, request
# from flask_restful import Resource, Api
from flask_pymongo import PyMongo

from flask_apscheduler import APScheduler

from thumb_download_thread import ThumbDownloadThread

app = Flask(__name__)
# api = Api(app)

app.config['MONGO_DBNAME'] = 'freeiptv'

app.config['MONGO_URI'] = 'mongodb://localhost:27070/freeiptv'

app.config.update(
    MONGO_HOST='localhost',
    MONGO_PORT=27017,
    MONGO_USERNAME='',
    MONGO_PASSWORD='',
    MONGO_DBNAME='freeiptv'
)


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


def thumb_index_job():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # M3u8Downloader(url=m3u8_url, path=download_path).start()

    oneday_time = time.mktime(datetime.datetime.now().timetuple()) - 60*60*24;

    thumb_query = {"$or": [{"thumb_time": {"$exists": False}},  {"$and": [{"thumb": {"$eq": ''}}, {"thumb_time": {"$lt": oneday_time}}]}]}

    # thumb_query = {"$or":[{"thumb": {"$exists": False}}, {"thumb_time": {"$lt": oneday_time}}]}
    # thumb_query = {"$or":[{"thumb": {"$exists": False}}, {"thumb_time": {"$lt": oneday_time}}]}
    # thumb_query = {"thumb": {"$exists": False}}

    result = mongo.db.playitems.find(thumb_query).limit(1)



    # output = []
    for s in result:
        # print(JSONEncoder().encode(s))
        # output.append(s)
        ThumbDownloadThread(s['_id'], s['url'], thumb_path, mongo).start()

    print(result.count())

    # print(JSONEncoder().encode(output))
    # for doc in result:
    #     print(JSONEncoder.encode(doc))


    # doc = {
    #     "url": url,
    #     "thumb_time": time.mktime(datetime.datetime.now().timetuple()),
    #     "thumb": thumb
    # }
    # return mongo.db.playitems.update_one(myquery, {'$set': doc}, upsert=True)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


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
    app.debug = True

    scheduler = APScheduler()
    # it is also possible to enable the API directly
    # scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()

    app.run(use_reloader=False)
