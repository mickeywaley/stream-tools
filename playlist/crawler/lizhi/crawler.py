import re

from playlist.crawler.lizhi.url_crawler import UrlCrawler
from playlist.crawler.lizhi.url_parser import UrlParser


tag_filter = lambda tag: tag.name == 'a' and len(tag.find_all("p")) > 0
attr_filter = lambda x: x.has_attr('title')
url_name_getter = lambda tag: tag.find_all("p")[0].get_text()

result_map = {}

url_parser = UrlParser(tag_filter=tag_filter,
                       attr_filter=attr_filter,
                       url_name_getter=url_name_getter)

crawler = UrlCrawler(parser=url_parser)
crawler.crawl('http://www.lizhizu.com/channel/cctv')


print(crawler.url_map)
#
# html = crawler.curl('http://www.lizhizu.com/player?id=5&val=1')
# tag_filter = lambda tag: tag.name == 'a'
attr_filter = lambda x: x.has_attr('onclick') and x.has_attr('data-player')
url_getter = lambda tag: tag.attrs['data-player']
url_parser = UrlParser(
                       attr_filter=attr_filter, url_getter=url_getter)

def url_mapper(url):
    parts = url.split('_')
    return 'http://www.lizhizu.com/player?id={}&val={}'.format(parts[0], parts[1])

inner_tag_filter = lambda tag: tag.name == 'script' and not tag.has_attr('src')

inner_attr_filter = lambda x: True

def inner_url_getter(tag):
    s = tag.get_text()
    left = s.find('$http')
    right = s.find('$m3u8')
    if right > left and left > 0:
        result=  s[left + 1:right]
        print(result)
        return result
    return None
inner_url_name_getter = lambda x: None

inner_url_parser = UrlParser(tag_filter=inner_tag_filter,
    attr_filter=inner_attr_filter, url_getter=inner_url_getter, url_name_getter=inner_url_name_getter)

# '信号1$http://223.110.243.168/PLTV/2510088/224/3221227343/1.m3u8$m3u8'
for url, name in crawler.url_map.items():
    print('{} :{}'.format(url, name))
    result_map[name] = {}
    crawler = UrlCrawler(parser=url_parser, debug=False)
    crawler.crawl(url)

    url_map = { url_mapper(k):crawler.url_map[k] for k in sorted(crawler.url_map)}

    for inner_url, inner_name in url_map.items():
        result_map[name][inner_name] = []

        inner_crawler = UrlCrawler(parser=inner_url_parser, debug=False)
        inner_crawler.crawl(inner_url)

        for m3u8 in inner_crawler.url_map.keys():
            result_map[name][inner_name].append(m3u8)


print(result_map)









