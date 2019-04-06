import os
import urllib
from urllib.request import Request, urlopen

from playlist.crawler.common.playlist_crawler import PlaylistCrawler
from playlist.crawler.common.url_crawler import UrlCrawler
from playlist.crawler.common.url_parser import UrlParser
from playlist.crawler.iptv201.langconv import Converter


class Iptv201PlaylistCrawler(PlaylistCrawler):
    def __init__(self):
        super().__init__()

    #
    # def urlParsing(self, uri) :
    #
    #     vid = uri[uri.index("://") + 3]
    #     if (uri.indexOf("http://") == 0) :
    #         if (uri.indexOf("") > -1) :
    #             uri = uri.replace("http://m.iptv789.com/player.m3u8", "http://cdn.iptv888.com:888/play.m3u8")
    #             uri = uri.replace("http://m.iptv.com/player.m3u8", "http://api2.iptv888.com/play.m3u8")
    #         return uri
    #     # elif (uri.indexOf("hunantv://") == 0) :
    #     #     url = "http://mpp.liveapi.mgtv.com/v1/epg/turnplay/getLivePlayUrlMPP?version=PCweb_1.0&platform=5&buss_id=2000001&channel_id=" + vid + "&definition=std"
    #     #     html = UrlCrawler.curl(url)
    #     #     return obj.data.url
    #     #
    #     # elif (uri.indexOf("pplive://") == 0) :
    #     #     ppurl = "http://play.api.pptv.com/boxplay.api?id=300146&type=m3u8.web.phone&gslbversion=2&ft=2&version=4&userLevel=1&appver=4.2.5&appid=com.pptv.iphoneapp&playback=0&o=pub.pptv.com"
    #     #     if (vid.length > 15) :
    #     #         $.getJSON("http://play.api.pptv.com/boxplay.api?id=300146&type=m3u8.web.phone&gslbversion=2&ft=2&version=4&userLevel=1&appver=4.2.5&appid=com.pptv.iphoneapp&playback=0&o=pub.pptv.com&callback=?", function(text) :
    #     #         host = ps(text, "<sh limit=\"(.*?)\">(.*?)</sh>", 2)
    #     #         kk = ps(text, "<key expire=\"(.*?)\">(.*?)</key>", 2)
    #     #         puri = "http://" + host + "/live/5/30/" + vid + ".m3u8?playback=0&pre=ikan&o=pub.pptv.com&type=m3u8.web.phone&k=" + kk
    #     #         setPlayerUri(puri)
    #     #      else:
    #     #             setPlayerUri("http://web-play.pptv.com/web-m3u8-" + vid + ".m3u8?type=m3u8.web.phone&playback=0&o=pub.pptv.com")
    #     #
    #     #
    #     #
    #     # elif uri.indexOf("://") > 2 :
    #     #     return uri
    #

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

            charset = self.url_parser.charset

            if response.headers.get_content_charset():
                charset = response.headers.get_content_charset()
                res = response.read().decode(charset, 'ignore')

                print("===get_url {} result:{}".format(url,res))
                return res
        except Exception as e:
            print("error %s: %s" % (url, e))
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
        url_parser = UrlParser(tag_filter=tag_filter, url_getter=url_getter )

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






