__author__ = 'gaoguanghe'
from bs4 import BeautifulSoup
import os, sys, urllib2,time,random,string,Tkinter,tkMessageBox
reload(sys)
sys.setdefaultencoding('utf-8')
global list
list=[]
flag = False
def getNewTpy():
    targetUrl = 'http://ks.pconline.com.cn/bbs.shtml?forumValue=240027&q=5s+%C8%FD%CD%F8&scope=all&pageNo=1'
    content = urllib2.urlopen(targetUrl)
    soup = BeautifulSoup(content,from_encoding='GB18030')
    nav = soup.select('.iTimeIcon')
    titles = soup.select(".blue")
    for t in titles:
        a = t["href"]+'\n'+t.text
        if a not in list:
            list.insert(0,a)
            print(a)
            if flag:
                tkMessageBox.showinfo("",a)
getNewTpy()
flag=True
while True:
    time.sleep(60)
    getNewTpy()
    print("\n")
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

