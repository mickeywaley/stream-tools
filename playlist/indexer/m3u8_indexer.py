import pymongo


class M3u8Indexer:
    def __init__(self, mongodb_url, db_name, collection_name):
        self.mongodb_url = mongodb_url
        self.mongo_client = pymongo.MongoClient(mongodb_url)
        self.data_list = self.mongo_client[db_name][collection_name]

    def find_all(self):
        return self.data_list.find()

    def find_by_url(self, url):
        myquery = {"url": url}
        return self.data_list.find_one(myquery)

    def update_thumb(self, url, thumb):
        myquery = {"url": url}
        newvalues = {"$set": {"thumb": thumb}}
        self.data_list.update_one(myquery, newvalues)

    def save(self, url='', name='', thumb='', category='', tag=''):
        myquery = {"url": url}

        doc = {
            "url": url,
            "name": name,
            "thumb": thumb
        }
        return self.data_list.update_one(myquery, {'$set': doc, '$addToSet': {'categories': category,
                                                        'tags': tag}}, upsert=True)

    def delete(self, url):
        myquery = {"url": url}

        self.data_list.delete_one(myquery)

    def delete_all(self):
        self.data_list.delete_many({})


if __name__ == '__main__':
    mongo_url = 'mongodb://192.168.2.26:32727/replicaSet=rs0'
    indexer = M3u8Indexer(mongo_url, 'playlist', 'm3u8')

    # indexer.delete_all()
    #
    # indexer.save('url', 'new name', 'new thumb', 'new cat', 'new tag2')

    for item in indexer.find_all():
        indexer.save(item['url'], 'new name', 'new thumb', 'new cat', 'new tag2')

    print(list(indexer.find_all()))
