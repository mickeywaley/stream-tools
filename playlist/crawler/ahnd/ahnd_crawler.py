from functools import cmp_to_key
from urllib.parse import urlparse, parse_qs

from playlist.crawler.ahnd.ahnd_url_crawler import Crawler


def getm3u8(url):
    u_parse = urlparse(url)

    params = dict(parse_qs(u_parse.query))

    params = {k: v[0] for k, v in params.items()}
    # print(params)

    channel = params.get("channel")
    server = params.get("server")
    type = params.get("type")

    if not channel:
        channel = ''

    if not server:
        server = ''

    if not type:
        type = ''

    # print('channel:%s\nserver:%s\ntype:%s\n' % (channel, server, type))

    if channel[0:7] == "rtmp://" or channel[0:7] == "http://":
        return channel

    if server == "":
        preStr = "http://" + u_parse.netloc + "/"
    else:
        preStr = "http://" + u_parse.netloc + ":8" + server + "/"

    if type == "":
        return preStr + "hls/" + channel + ".m3u8"

    if type == "hlsp":
        return preStr + "hls/" + channel + "/playlist.m3u8"

    if type == "hlsi":
        return preStr + "hls/" + channel + "/index.m3u8"

    if type == "lived":
        return preStr + "live/" + channel + ".m3u8"

    if type == "livexd":
        return preStr + "live/" + channel + "/" + channel + ".m3u8"

    if type == "liven":
        return preStr + "live/" + channel + "/.m3u8"

    if type == "livep":
        return preStr + "live/" + channel + "/playlist.m3u8"

    if type == "livei":
        return preStr + "live/" + channel + "/index.m3u8"

    if type == "livet":
        return preStr + "live/" + channel + "/tzwj_video.m3u8"

    if type == "n":
        return preStr + channel + ".m3u8"

    if type == "nx":
        return preStr + channel

    if type == "nf":
        return preStr + channel + ".flv"

    if type == "p":
        return preStr + channel + "/playlist.m3u8"

    if type == "i":
        return preStr + channel + "/index.m3u8"

    if type == "l":
        return preStr + channel + "/live.m3u8"

    if type == "xxxs":
        return preStr + channel + "/sd/live.m3u8"

    if type == "xxxh":
        return preStr + channel + "/hd/live.m3u8"

    if type == "tsls":
        return preStr + "tslslive/" + channel + "/hls/live_sd.m3u8"

    if type == "chnnetcq":
        return preStr + "PLTV/88888888/224/322122" + channel + "/chunklist.m3u8"

    if type == "cmcc88":
        return preStr + "PLTV/88888888/224/322122" + channel + "/index.m3u8"

    if type == "cmccsy":
        return preStr + "hwottcdn.ln.chinamobile.com/PLTV/88888890/224/322122" + channel + "/index.m3u8"

    if type == "cmcchb":
        return preStr + "huaweicdn.hb.chinamobile.com/PLTV/2510088/224/322122" + channel[0:4] + "/" + channel[
                                                                                                      4:5] + ".m3u8"

    if type == "cmccxa":
        return preStr + "dbiptv.sn.chinamobile.com/PLTV/88888890/224/322122" + channel + "/index.m3u8"

    if type == "cmccnj":
        return preStr + "PLTV/" + channel[0:1] + "/224/322122" + channel[1:5] + "/2.m3u8"

    if type == "cmccjs":
        return preStr + "ott.js.chinamobile.com/PLTV/3/224/322122" + channel + "/index.m3u8"

    if type == "cmcccl":
        return preStr + "PLTV/88888888/224/322122" + channel + "/chunklist.m3u8"

    if type == "lec":
        return preStr + "live/hls/" + channel + "/desc.m3u8"

    if type == "aodytv":
        return preStr + "tv_radio_" + channel[0:5] + "/tv_channel_" + channel[5] + "__redirect__" + channel[
                                                                                                    0:5] + ".m3u8"

    if type == "aodylm":
        return preStr + "lms_" + channel[0:5] + "/tv_channel_" + channel[5] + "__redirect__" + channel[0:5] + ".m3u8"

    if type == "aodygd":
        return preStr + "guangdianyun_" + channel[0:5] + "/tv_channel_" + channel[5] + "__redirect__" + channel[
                                                                                                        0:5] + ".m3u8"

    if type == "cjybc":
        return preStr + "video/s10" + channel + "/index.m3u8"

    if type == "cucc":
        return preStr + "gitv_live/" + channel + "/" + channel + ".m3u8"

    if type == "chxl":
        return preStr + "channels/" + channel + "/live.flv"

    if type == "chxlm":
        return preStr + "channels/" + channel + "/m3u8:500k/live.m3u8"

    if type == "ah05":
        return preStr + "channels/preview/" + channel + "/m3u8:500k/live.m3u8"

    if type == "ah06":
        return preStr + "channels/39/500.flv"

    if type == "zgjt":
        return preStr + "zgjt/beijing.m3u8?auth_key=1701185783-0-0-e36f09598d451ea4440bbd83411e7fd5"

    if type == "zgjtah":
        return preStr + "zgjt/zgjtah.m3u8?auth_key=1893430861-0-0-d46bdf4ba08863c373461a56e8057d56"

    if type == "zgjthb":
        return preStr + "zgjt/zgjthb.m3u8?auth_key=1893430861-0-0-f7357974c29e0b417e899dc47121337c"

    if type == "yntv":
        return preStr + "channels/yn/" + channel + "/m3u8:sd/live.m3u8"

    if type == "nm05":
        return preStr + "channels/btgd/" + channel + "/m3u8:500k/live.m3u8"

    if type == "njtv":
        return preStr + "channels/njtv/" + channel + "/m3u8:500k/live.m3u8"

    if type == "nttv":
        return preStr + "channels/nttv/" + channel + "/m3u8:SD/live.m3u8"

    if type == "lantian":
        return preStr + "channels/lantian/channel" + channel + "/360p.m3u8"

    if type == "sihtv":
        return preStr + "channels/tvie/" + channel + "/m3u8:500k/live.m3u8"

    if type == "cooldiao":
        return preStr + "cmstop/s10001-video-" + channel + ".m3u8"

    if type == "nnlivef":
        return preStr + "nn_live.flv?id=" + channel

    if type == "rtmp":
        return "rtmp://" + u_parse.netloc + "/ahau/" + channel

    return "http://" + u_parse.netloc + "/hls/cctv5.m3u8"

    pass


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


def generate_m3u8_file(channel_map):
    for channel, url in channel_map.items():
        print("{}:{}".format(channel, url))

    with open('playlist.m3u8', 'wb') as f:

        f.write(b'#EXTM3U\n\n')

        for channel, urls in channel_map.items():
            name = '#EXTINF:-1,' + channel + '\n'

            for url in urls:
                link = getm3u8(url) + '\n\n'

                f.write(name.encode(encoding='utf8'))
                f.write(link.encode(encoding='utf8'))


crawler = Crawler()
crawler.crawl('http://itv.ahau.edu.cn')

channel_map = crawler.channel_map
#
# for k in
#
# channels = sorted(channel_map, key=cmp_to_key(channel_sort), reverse=False)

channel_map = {k: channel_map[k] for k in sorted(channel_map, key=cmp_to_key(channel_sort), reverse=False)}


generate_m3u8_file(channel_map)
