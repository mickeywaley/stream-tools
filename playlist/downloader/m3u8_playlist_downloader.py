import os

import requests

from playlist.downloader import m3u8_downloader

"""
下载M3U8文件里的所有片段
"""


def download(url):
    download_path = os.getcwd() + "/download"

    if not os.path.exists(download_path):
        os.mkdir(download_path)

    all_content = requests.get(url).text  # 获取M3U8的文件内容
    file_line = all_content.split("\n")  # 读取文件里的每一行
    # 通过判断文件头来确定是否是M3U8文件
    if file_line[0] != "#EXTM3U":
        raise BaseException(u"非M3U8的链接")

    for index, line in enumerate(file_line):
        if "EXTINF" in line:
            # 拼出ts片段的URL
            pd_url = file_line[index + 1]

            m3u8_downloader.download(pd_url, download_path)


if __name__ == '__main__':
    download("https://raw.githubusercontent.com/lizhiyong2000/stream-tools/master/resource/ahnd-playlist.m3u8")