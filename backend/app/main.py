import os

from flask import Flask, request, Blueprint
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo

from common import JSONEncoder
from config import Config
from log import config_root_logger
from thumb_download_thread import ThumbIndexJob


from datetime import datetime

from flask import Flask, jsonify, request, Blueprint
from flask_mongoengine import MongoEngine
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

from datetime import datetime


app = Flask(__name__)

app.config['MONGO_DBNAME'] = Config.MONGO_DBNAME
app.config['MONGO_URI'] = Config.MONGO_URI


app.config['MONGODB_SETTINGS'] = {
    'db': 'freeiptv',
    'host': 'localhost',
    'port': 27070
}

db = MongoEngine(app)




class User(db.Document):
    user_id = db.IntField(required=True)
    name = db.StringField(required=True, max_length=100)
    email = db.StringField(max_length=200)
    pwd = db.StringField(requied=True, min_length=6)
    createtime = db.DateTimeField(required=True)

    def to_json(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email
        }

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)

login_manager = LoginManager()
login_manager.init_app(app)


app.config['JOBS'] = [
    {
        'id': 'thumb_index_job',
        'func': 'main:thumb_index_job',
        'trigger': 'interval',
        'seconds': 3
    }
]

app.config['SCHEDULER_API_ENABLED'] = True

user_blueprint = Blueprint('users', __name__)

app.register_blueprint(user_blueprint, url_prefix='/users')

mongo = PyMongo(app)

filepath = os.path.abspath(__file__)

thumb_path = os.path.join(os.path.dirname(filepath), "../../nginx/dist/images/thumbs")

thumb_index_job = ThumbIndexJob(thumb_path, mongo)

thumb_index_job.setName("THUMB_MAIN")


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

        # print(s['_id'])





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

    # print(count)

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

    # print(count)

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




@login_manager.user_loader
def load_user(user_id):
    return User.objects(user_id=user_id).first()


@app.route('/register', methods=['POST'])
def registerUser():
    if not request.json or not 'name' in request.json or not 'pwd' in request.json:
        return jsonify({'err': 'Request not Json or miss name/pwd'})
    elif User.objects(name=request.json['name']).first():
        return jsonify({'err': 'Name is already existed.'})
    else:
        user = User(
            user_id=User.objects().count() + 1,
            name=request.json['name'],
            email=request.json['email'] if 'email' in request.json else "",
            pwd=request.json['pwd'],
            createtime=datetime.now()
        )
        try:
            user.save()
        except Exception:
            return jsonify({'err': 'Register error.'})
    return jsonify({'status': 0, 'user_id': user['user_id'], 'msg': 'Register success.'})


@app.route('/login', methods=['POST'])
def login():
    if not request.json or not 'name' in request.json or not 'pwd' in request.json:
        return jsonify({'err': 'Request not Json or miss name/pwd'})
    else:
        user = User.objects(
            name=request.json['name'], pwd=request.json['pwd']).first()
    if user:
        login_user(user)
        return jsonify({'status': 0, 'user_id': user.get_id(), 'msg': 'Login success.'})
    else:
        return jsonify({'err': 'Login fail.'})


@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({'status': 0, 'msg':'Logout success.'})


@app.route('/user', methods=['GET'])
def getUser():
    if current_user.is_authenticated:
        return jsonify({'status': 0, 'user': current_user.to_json()})
    else:
        return jsonify({'err': 'Not login.'})


@app.route('/user/email', methods=['PUT'])
@login_required
def putUserEmail():
    if not request.json or not 'email' in request.json:
        return jsonify({'err': 'Request not Json or miss email'})
    else:
        current_user.email = request.json['email']
        try:
            current_user.save()
        except Exception:
            return jsonify({'err': 'Modify email error.'})
        return jsonify({'status': 0, 'msg': 'Email has been modified.', 'user': current_user.to_json()})


@app.route('/user/pwd', methods=['PUT'])
@login_required
def putUserPWD():
    if not request.json or not 'current_pwd' in request.json or not 'new_pwd' in request.json:
        return jsonify({'err': 'Request not Json or miss current_pwd/new_pwd'})
    else:
        current_pwd = current_user.pwd
    if not request.json['current_pwd'] == current_pwd:
        return jsonify({'err': 'current_pwd is not right.'})
    else:
        current_user.pwd = request.json['new_pwd']
        try:
            current_user.save()
        except Exception:
            return jsonify({'err': 'Modify PWD error.'})
        return jsonify({'status': 0, 'msg': 'PWD has been modified.', 'user_id': current_user.user_id})



if __name__ == '__main__':

    config_root_logger()

    app.debug = True
    app.run()
