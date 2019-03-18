
from playlist.crawler.lizhi.url_crawler import UrlCrawler
from playlist.crawler.lizhi.url_parser import UrlParser


def url_tag_filter(tag):
    return tag.name == 'a' and len(tag.find_all("p")) > 0


def url_name_getter(tag):
    return tag.find_all("p")[0].get_text()


url_parser = UrlParser(tag_filter=url_tag_filter, attr_filter=lambda x:x.has_attr('title'), url_name_getter=url_name_getter)

crawler = UrlCrawler(parser=url_parser)
crawler.crawl('http://www.lizhizu.com/channel/cctv')

crawler.url_map
