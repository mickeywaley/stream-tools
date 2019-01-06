import requests
import time
t1 = time.time()
URL = 'http://www.szmgiptv.com:14436/hls/{}.m3u8'
print('开始！')
for n in range(0,66):
    url = URL.format(str(n))
    try:
        r=requests.get(url)
        if '200' in str(r):
            print(str(n) + ',' + url)
        else:
            pass
    except requests.exceptions.ConnectionError:
        pass
print('完成！')
t2 =time.time()
print(t2 - t1)