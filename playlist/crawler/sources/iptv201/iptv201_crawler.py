import urllib

from playlist.crawler.common.url_crawler import UrlCrawler
from playlist.crawler.common.url_parser import UrlParser
from playlist.crawler.sources.iptv201.iptv201_playlist_crawler import Iptv201PlaylistCrawler
from playlist.crawler.sources.iptv201.langconv import Converter


def tag_filter(tag):
    result = (tag.name == 'a' and tag.has_attr('href'))

    if not result:
        return result

    href = tag.attrs['href']

    if href:
        return href.startswith('?tid=')

    return False

# url_name_getter = lambda tag: tag.find_all("p")[0].get_text()

url_parser = UrlParser(tag_filter=tag_filter)

crawler = UrlCrawler(parser=url_parser)

base_url = 'http://iptv201.com'
crawler.crawl(base_url)

converter = Converter('zh-hans')


def url_mapper(url):
    return urllib.parse.urljoin(base_url, url)


url_map = {url_mapper(k): converter.convert(crawler.url_map[k]) for k in sorted(crawler.url_map)}

playlistCrawler = Iptv201PlaylistCrawler()

print(url_map)

for url, name in url_map.items():

    playlistCrawler.crawl(name, url, root_url=base_url)





