import json

from bson import ObjectId
from flask import Flask, jsonify, request
# from flask_restful import Resource, Api
from flask_pymongo import PyMongo

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

mongo = PyMongo(app)


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

    page_size = 20 if not request.args.get('pageSize') or  not is_number(request.args.get('pageSize')) else int(request.args.get('pageSize'))

    skip = (page_num - 1)*page_size

    query = []
    if channel:
        channel_query = {"channel": {"$eq": channel}}
        query.append(channel_query)
    if keyword:
        keyword_query = {"tags": {"$elemMatch": {"$regex": ".*{}.*".format(keyword), "$options": "i"}}}
        query.append(keyword_query)

    if len(query) > 0:
        result = mongo.db.playitems.find({"$and": query})
    else:
        result = mongo.db.playitems.find()

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

    output = []
    for s in result:
        output.append(s)

    return JSONEncoder().encode(output)


if __name__ == '__main__':
    app.debug = True
    app.run()
