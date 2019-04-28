import datetime
import time

from playlist.scheduler.crawler_scheduler import CrawlerScheduler




if __name__ == '__main__':

    print(time.mktime(datetime.datetime.now().timetuple()))



    scheduler = CrawlerScheduler()
    scheduler.run()