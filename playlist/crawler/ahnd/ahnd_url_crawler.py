# -*- coding: utf-8 -*-
# filename: ahnd_url_crawler.py

import ssl
import urllib
from html.parser import HTMLParser
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ssl._create_default_https_context = ssl._create_unverified_context


class AhndHrefParser(HTMLParser):
    """
    Parser that extracts hrefs
    """
    is_parsing_url = False
    parsing_url = None

    url_channel_names = dict()

    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            dict_attrs = dict(attrs)
            if dict_attrs.get('href'):
                href = dict_attrs['href']
                if href.startswith('aplayer.html'):
                    self.parsing_url = href
                    self.is_parsing_url = True
                    # self.hrefs.add(dict_attrs['href'])

    def handle_endtag(self, tag):
        self.parsing_url = None
        self.is_parsing_url = False

    def handle_data(self, data):
        if self.is_parsing_url:
            print("channel:{}, url:{}".format(data, self.parsing_url))
            self.url_channel_names[self.parsing_url] = data


class Crawler(object):

    def __init__(self):
        """
        depth: how many time it will bounce from page one (optional)
        cache: a basic cache controller (optional)
        """
        self.channel_map = {}
        self.request_url = ''

    def crawl(self, url):
        """
        url: where we start crawling, should be a complete URL like
        'http://www.intel.com/news/'
        no_cache: function returning True if the url should be refreshed
        """
        self.request_url = url
        # self._crawl([u_parse.path], self.depth)
        print(" to crawl url:%s" % url)

        self._crawl(url)

    # def get(self, url):
    #     page = self.curl(url)
    #     return page

    def _crawl(self, url):
        html = self.curl(url)
        # self.set(url, html)

        self.get_channel_urls(url, html)

    def curl(self, url):
        """
        return content at url.
        return empty string if response raise an HTTPError (not found, 500...)
        """
        try:
            print("retrieving url... %s" % (url))
            # req = Request('%s://%s%s' % (self.scheme, self.domain, url))
            req = Request(url)

            response = urlopen(req)
            return response.read().decode('gb2312', 'ignore')
        except HTTPError as e:
            print("error [%s] %s: %s" % (self.domain, url, e))
            return ''

    def get_channel_urls(self, url, html):
        """
        Read through HTML content and returns a tuple of links
        internal to the given domain
        """
        parser = AhndHrefParser()
        parser.feed(html)

        #
        # self.channel_map = parser.url_channel_names
        url_to_channel_map = {urllib.parse.urljoin(url, k): v for k, v in parser.url_channel_names.items()}

        for url, channel in url_to_channel_map.items():
            self.add_channel(channel, url)

    def add_channel(self, channel, url):

        try:
            urls = self.channel_map[channel]
        except KeyError:
            urls = []

        urls.append(url)

        self.channel_map[channel] = urls
