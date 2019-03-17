# -*- coding: utf-8 -*-
# filename: ahnd_url_crawler.py

import ssl
import urllib
from html.parser import HTMLParser
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ssl._create_default_https_context = ssl._create_unverified_context


class Iptv201GroupHrefParser(HTMLParser):
    """
    Parser that extracts hrefs
    """
    def __init__(self):
        super().__init__()
        self.is_parsing_url = False
        self.parsing_url = None

        self.url_channel_names = dict()

    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            dict_attrs = dict(attrs)
            if dict_attrs.get('href'):
                href = dict_attrs['href']
                if href.startswith('?tid='):
                    self.parsing_url = href
                    self.is_parsing_url = True
                    # self.hrefs.add(dict_attrs['href'])

    def handle_endtag(self, tag):
        self.parsing_url = None
        self.is_parsing_url = False

    def handle_data(self, data):
        if self.is_parsing_url:
            # print("channel:{}, url:{}".format(data, self.parsing_url))
            self.url_channel_names[self.parsing_url] = data


class Iptv201HrefParser(HTMLParser):
    """
    Parser that extracts hrefs
    """
    def __init__(self):
        super().__init__()
        self.is_parsing_url = False
        self.parsing_url = None

        self.url_channel_names = dict()

    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            dict_attrs = dict(attrs)
            if dict_attrs.get('href'):
                href = dict_attrs['href']
                if href.startswith('?act=play'):
                    self.parsing_url = href
                    self.is_parsing_url = True
                    # self.hrefs.add(dict_attrs['href'])

    def handle_endtag(self, tag):
        self.parsing_url = None
        self.is_parsing_url = False

    def handle_data(self, data):
        if self.is_parsing_url:
            # print("channel:{}, url:{}".format(data, self.parsing_url))
            self.url_channel_names[self.parsing_url] = data


class Iptv201PlaylistParser(HTMLParser):
    """
    Parser that extracts hrefs
    """
    def __init__(self):
        super().__init__()
        self.is_parsing_url = False
        self.parsing_url = None

        self.url_channel_names = dict()

    def handle_starttag(self, tag, attrs):

        if tag == 'option':
            dict_attrs = dict(attrs)
            if dict_attrs.get('value'):
                href = dict_attrs['value']
                self.parsing_url = href
                self.is_parsing_url = True
                    # self.hrefs.add(dict_attrs['href'])

    def handle_endtag(self, tag):
        self.parsing_url = None
        self.is_parsing_url = False

    def handle_data(self, data):
        if self.is_parsing_url:
            # print("channel:{}, url:{}".format(data, self.parsing_url))
            self.url_channel_names[self.parsing_url] = data


class Crawler(object):

    def __init__(self):
        """
        depth: how many time it will bounce from page one (optional)
        cache: a basic cache controller (optional)
        """
        self.channel_map = {}
        self.request_url = ''
        self.channel_group = {}

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

        parser = Iptv201GroupHrefParser()
        parser.feed(html)

        #
        # self.channel_map = parser.url_channel_names
        url_to_channel_map = {urllib.parse.urljoin(self.request_url, k): v for k, v in parser.url_channel_names.items()}

        for url, channel in url_to_channel_map.items():
            self.add_channel_group(channel)
            self._crawl_channel_group(channel, url)

        print("{} crawled".format(url))


    def _crawl_channel_group(self, channel_group, url):

        html = self.curl(url)

        parser = Iptv201HrefParser()
        parser.feed(html)

        #
        # self.channel_map = parser.url_channel_names
        url_to_channel_map = {urllib.parse.urljoin(self.request_url, k): v for k, v in parser.url_channel_names.items()}

        for url, channel in url_to_channel_map.items():
            self.add_channel_to_group(channel_group, channel)
            self._crawl_single_channel(channel_group, channel, url)

        print("channel group:{} crawled".format(channel_group))
        pass

    def _crawl_single_channel(self, group, channel, url):
        html = self.curl(url)

        parser = Iptv201PlaylistParser()
        parser.feed(html)

        url_to_channel_map = {urllib.parse.urljoin(self.request_url, k): v for k, v in parser.url_channel_names.items()}

        for url, channel in url_to_channel_map.items():

            channel_url = self.curl(url)

            self.add_channel(group, channel, channel_url)
        print("{}:{} crawled".format(group, channel))

    def curl(self, url):
        """
        return content at url.
        return empty string if response raise an HTTPError (not found, 500...)
        """
        try:
            print("retrieving url... %s" % (url))
            # req = Request('%s://%s%s' % (self.scheme, self.domain, url))
            req = Request(url)

            req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.i/605.1.15')

            response = urlopen(req, timeout=1)

            if response.url != req.full_url:
                return response.url
            return response.read().decode(response.headers.get_content_charset(), 'ignore')
        except Exception as e:
            print("error %s: %s" % (url, e))
            return ''

    def add_channel(self, group, channel, url):

        try:
            urls = self.channel_group[group][channel]
        except KeyError:
            urls = []

        if len(url) > 0:
            print("add {}-{}:{}".format(group, channel, url))
            urls.append(url)

        self.channel_group[group][channel] = urls

    def add_channel_to_group(self, group, channel):
        channels = self.channel_group[group]
        channels[channel] = []

    def add_channel_group(self, group):
        self.channel_group[group] = {}


