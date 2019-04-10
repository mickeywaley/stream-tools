import pymongo

connection = pymongo.MongoClient('192.168.2.26', 32717)
db = connection.playlist
m3u8 = db.m3u8
m3u8.insert({'url': "李白", "name":"", "tags": [], "source": "Python", "thumb": ""})
print("操作完成")


