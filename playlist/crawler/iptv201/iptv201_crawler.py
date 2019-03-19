from functools import cmp_to_key
from playlist.crawler.iptv201.iptv201_url_crawler import Crawler
from playlist.crawler.iptv201.langconv import Converter


def channel_sort(first, second):
    pattern = '';
    if first.startswith('CCTV') and second.startswith('CCTV'):
        # pattern = 'CCTV(\d+)'
        #
        # ch1 = re.search(pattern, first)

        result = (lambda a, b: (a > b) - (a < b))(first, second)

        # print("1{} {} {}".format(first, '>' if result > 0 else '<', second))
        return result
    else:
        if first.startswith('CCTV'):
            # print("2{} {} {}".format(first, '<', second))
            return -1
        if second.startswith('CCTV'):
            # print("3{} {} {}".format(first, '>', second))
            return 1

    if first.startswith('《') and second.startswith('《'):
        result = (lambda a, b: (a > b) - (a < b))(first, second)

        # print("4{} {} {}".format(first, '>' if result > 0 else '<', second))
        return result
    else:
        if first.startswith('《'):
            # print("5{} {} {}".format(first, '>', second))
            return 1
        if second.startswith('《'):
            # print("6{} {} {}".format(first, '<', second))
            return -1

    if first.endswith('卫视') and second.endswith('卫视'):
        result = (lambda a, b: (a > b) - (a < b))(first, second)

        # print("7{} {} {}".format(first, '>' if result > 0 else '<', second))
        return result
    else:
        if first.endswith('卫视'):
            # print("8{} {} {}".format(first, '<', second))
            return -1
        if second.endswith('卫视'):
            # print("9{} {} {}".format(first, '>', second))
            return 1

    result = (lambda a, b: (a > b) - (a < b))(first, second)

    # print("10{} {} {}".format(first, '>' if result > 0 else '<', second))
    return result


def generate_m3u8_file(group, channel_map):
    for channel, url in channel_map.items():
        print("{}:{}".format(channel, url))

    converter = Converter('zh-hans')

    with open('{}-playlist.m3u8'.format(converter.convert(group)), 'wb') as f:

        f.write(b'#EXTM3U\n\n')

        for channel, urls in channel_map.items():
            name = '#EXTINF:-1,' + converter.convert(channel) + '\n'

            for url in urls:
                link = url + '\n\n'

                f.write(name.encode(encoding='utf8'))
                f.write(link.encode(encoding='utf8'))


crawler = Crawler()
crawler.crawl('http://iptv201.com')

channel_group = crawler.channel_group
#
# for k in
#
# channels = sorted(channel_map, key=cmp_to_key(channel_sort), reverse=False)

for group, channel_map in channel_group.items():
    # channel_map = {k: channel_map[k] for k in sorted(channel_map, key=cmp_to_key(channel_sort), reverse=False)}
    channel_map = {k: channel_map[k] for k in channel_map}
    generate_m3u8_file(group, channel_map)
