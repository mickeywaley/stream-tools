# -*- coding: utf-8 -*-
# filename: ahnd_url_crawler.py

import ssl
from urllib.request import Request, urlopen

ssl._create_default_https_context = ssl._create_unverified_context


class UrlCrawler(object):

    def __init__(self, parser=None, url_mapper=lambda x: x):
        """
        depth: how many time it will bounce from page one (optional)
        cache: a basic cache controller (optional)
        """
        self.url_map = {}
        self.init_url = ''
        self.url_parser = parser
        self.url_mapper = url_mapper

    def crawl(self, url):
        """
        url: where we start crawling, should be a complete URL like
        'http://www.intel.com/news/'
        no_cache: function returning True if the url should be refreshed
        """
        self.init_url = url
        print(" to crawl url:%s" % url)

        html = self.curl(url)

        self.url_parser.parse(html)

    def curl(self, url):
        """
        return content at url.
        return empty string if response raise an HTTPError (not found, 500...)
        """
        try:
            print("retrieving url... %s" % (url))
            # req = Request('%s://%s%s' % (self.scheme, self.domain, url))
            req = Request(url)

            req.add_header('User-Agent',
                           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.i/605.1.15')

            response = urlopen(req, timeout=1)

            # print(response.encoding)

            if response.url != req.full_url:
                return response.url
            return response.read().decode(response.headers.get_content_charset(), 'ignore')
        except Exception as e:
            print("error %s: %s" % (url, e))
            return ''
