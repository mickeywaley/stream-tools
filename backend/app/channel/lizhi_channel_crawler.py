import pymongo

from channel.channel_crawler import ChannelCrawler
from channel.channel_parser import ChannelParser
from playlist.crawler.common.url_parser import UrlParser

result_map = {}

tag_filter = lambda tag: tag.name == 'div' and tag.has_attr('class') and tag.get('class')[0] == 'channel-item'
name_getter = lambda tag: tag.find_all("p")[0].get_text()

thumb_getter = lambda tag: "http://www.lizhizu.com{}".format(tag.find_all("img")[0].get('data-echo'))

channel_parser = ChannelParser(tag_filter=tag_filter,
                       name_getter=name_getter, thumb_getter=thumb_getter)


page_url_base = 'http://www.lizhizu.com/channel?p={}'

crawler = ChannelCrawler(parser=channel_parser)

for i in range(16, 0, -1):

    page_url = page_url_base.format(i)

    crawler.crawl(page_url)

    # print(crawler.channel_map)

    for name, thumb in crawler.channel_map.items():
        result_map[name] = thumb

print(result_map)

mongodb_url = 'mongodb://localhost:27017'
mongo_client = pymongo.MongoClient(mongodb_url)
data_list = mongo_client['freeiptv']['channels']


for name, thumb in result_map.items():

    print("[Index-Channel]: {}".format(name))
    myquery = {"name": name}

    doc = {
        "name": name,
        "thumb": thumb
    }
    data_list.update_one(myquery, {'$set': doc}, upsert=True)