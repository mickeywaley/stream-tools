import os
import urllib
from urllib.request import Request, urlopen

from playlist.crawler.common.playlist_crawler import PlaylistCrawler
from playlist.crawler.common.url_crawler import UrlCrawler
from playlist.crawler.common.url_parser import UrlParser
from playlist.crawler.sources.iptv201.langconv import Converter


class Iptv201PlaylistCrawler(PlaylistCrawler):
    def __init__(self):
        super().__init__()


    def get_url(self, url):

        try:
            print("retrieving url... %s" % (url))
            # req = Request('%s://%s%s' % (self.scheme, self.domain, url))
            req = Request(url)

            req.add_header('User-Agent',
                           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.i/605.1.15')

            response = urlopen(req, timeout=1)

            # print(response.encoding)

            if response.url != req.full_url:
                print("====get_url {} result:{}".format(url, response.url))
                return response.url

            charset = 'utf-8'

            if response.headers.get_content_charset():
                charset = response.headers.get_content_charset()
                res = response.read().decode(charset, 'ignore')

                # print("===get_url {} result:{}".format(url, res))
                return res
        except Exception as e:
            print("get_url error %s: %s" % (url, e))
            return ''

    def _crawl_page(self, page_url):

        converter = Converter('zh-hans')

        result_map = {}

        def tag_filter(tag):
            result = (tag.name == 'a' and tag.has_attr('href'))

            if not result:
                return result

            href = tag.attrs['href']

            if href:
                return href.startswith('?act=play')

            return False

        # url_name_getter = lambda tag: tag.find_all("p")[0].get_text()

        url_parser = UrlParser(tag_filter=tag_filter)

        crawler = UrlCrawler(parser=url_parser)

        crawler.crawl(page_url)

        def url_mapper(url):
            return urllib.parse.urljoin(self.root_url, url)

        url_map = {url_mapper(k): converter.convert(crawler.url_map[k]) for k in sorted(crawler.url_map)}

        print("playlist:{} channel map:{}".format(self.name, url_map))

        tag_filter = lambda tag: tag.name == 'option' and tag.has_attr('value')

        def url_getter(tag):
            return tag.attrs['value']
        url_parser = UrlParser(tag_filter=tag_filter, url_getter=url_getter)

        crawler = UrlCrawler(parser=url_parser, debug=False)

        for url, name in url_map.items():

            crawler.crawl(url)

            print("craw url:{} result map:{} ".format(url, crawler.url_map))

            if len(crawler.url_map.items()) == 0:
                raise Exception("Failed to get url")

            for m3u8 in crawler.url_map.keys():
                print('{} {}'.format(name, m3u8))


                # if m3u8 and m3u8.endswith('m3u8'):
                if name in result_map.keys():

                    result_map[name].append(m3u8)
                else:
                    result_map[name] = [m3u8]

                for inner_name, urls in result_map.items():
                    if len(urls) > 0:

                        urls = [self.get_url(u) for u in urls]
                        print("{} urls:{}".format(name, urls))
                        self.result_map[name] = urls






