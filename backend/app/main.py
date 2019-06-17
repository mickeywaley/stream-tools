import os

from flask import Flask, request
from flask_pymongo import PyMongo

from common import JSONEncoder
from config import Config
from thumb_download_thread import ThumbIndexJob

app = Flask(__name__)

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

thumb_index_job = ThumbIndexJob(thumb_path, mongo)


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

@app.route('/start_thumb')
def start_thumb():

    if not thumb_index_job.is_alive():

        thumb_index_job.start()

    return JSONEncoder().encode({
        "result": "started"
    })

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

    app.run()
