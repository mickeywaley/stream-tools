import os


class PlaylistCrawler:
    def __init__(self):
        self.result_map = {}
        self.name = ''
        self.base_url = ''

    def generate_m3u8_file(self):

        # converter = Converter('zh-hans')
        cwd = os.getcwd()
        with open(os.path.join(cwd, '{}-playlist.m3u8'.format(self.name)), 'wb') as f:

            f.write(b'#EXTM3U\n\n')

            for channel, urls in self.result_map.items():
                name = '#EXTINF:-1,' + channel + '\n'

                for url in urls:
                    link = url + '\n\n'

                    f.write(name.encode(encoding='utf8'))
                    f.write(link.encode(encoding='utf8'))







