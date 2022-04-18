#!/usr/bin/python3
import re
import threading
import time

import numpy as np
import requests
from bs4 import BeautifulSoup

exitFlag = 0
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/75.0.3770.100 Safari/537.36'}
mynews = []


class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.url_list = []
        url = "https://www.thepaper.cn/load_index.jsp?nodeids=90069,&channelID=108856&topCids=,&pageidx=" \
              + str(self.threadID) + "&lastTime=" + str(int(round(time.time() * 1000)))
        html = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(html.content, 'lxml')
        for a in soup.select('h2 > a'):
            url = "https://www.thepaper.cn/" + a["href"]
            self.url_list.append(url)
        self.url_list = np.unique(self.url_list)

    def run(self):
        for u in self.url_list:
            try:
                urlhtml = requests.get(url=u, headers=headers)
                urlsoup = BeautifulSoup(urlhtml.content, 'lxml')
                news = urlsoup.select(".news_txt")[0]
                title = urlsoup.select("title")[0]
                print(title.text + "  FORM 线程" + str(self.threadID))
                title_txt = re.sub(r'_[^_]*_[^_]*$', '', title.text)
                news_txt = news.text
                mynews.append((title_txt, u, news_txt))
                # print(title.text)
                # title_txt = re.sub(r'_[^_]*_[^_]*$', '', title.text)
                # news_txt = news.text
                # mynews.append((title_txt, u, news_txt))

            except:
                pass


def get_news():
    # 创建新线程
    thread1 = myThread(1, "Thread-1")
    thread2 = myThread(2, "Thread-2")
    thread3 = myThread(3, "Thread-3")
    thread4 = myThread(4, "Thread-4")
    thread5 = myThread(5, "Thread-5")
    thread6 = myThread(6, "Thread-6")
    thread7 = myThread(7, "Thread-7")
    thread8 = myThread(8, "Thread-8")
    thread9 = myThread(9, "Thread-9")
    thread10 = myThread(10, "Thread-9")
    thread11 = myThread(11, "Thread-9")
    thread12 = myThread(12, "Thread-9")
    thread13 = myThread(13, "Thread-9")
    thread14 = myThread(14, "Thread-9")
    thread15 = myThread(15, "Thread-9")
    thread16 = myThread(16, "Thread-9")

    # 开启新线程
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()
    thread12.start()
    thread13.start()
    thread14.start()
    thread15.start()
    thread16.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()
    thread11.join()
    thread12.join()
    thread13.join()
    thread14.join()
    thread15.join()
    thread16.join()

    print(mynews)
    # sqlHelper = sqlhelper.SqlHelper("localhost", "root", "123456", 3306, "hello")
    # sqlHelper.create_table("mynews", ["title", "url", "txt"])
    # sqlHelper.execute_manysql2('''INSERT INTO mynews (title,url,txt) VALUES (%s,%s,%s);''', mynews)


def connect_test():
    url = "https://www.thepaper.cn/load_index.jsp?nodeids=90069,&channelID=102407&topCids=,&pageidx=110000&lastTime=" \
          + str(int(round(time.time() * 1000)))
    html = requests.get(url=url, headers=headers)
    return html.status_code


start = time.time()
get_news()
end = time.time()
print(str(end - start))
