#-*- utf-8 -*-
#网址：
#http://www.biquge.cm/
#


import requests
import re
from lxml import etree


class biquge():
    url = "http://www.biquge.cm"

    txt = ""
    totalChapter = {}
    novelMessage = {"webname" : "笔趣阁"}

   #用于测试
    totalChapterList = []
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    }
    def __init__(self,novelName,detail=False):

       SearchUrl = "http://www.biquge.cm/modules/article/sou.php"
       key = self.EncodenovleName(novelName)
       body = {
           'si' :'biquge.cm' ,
           'sts' : 'biquge.cm',
           'searchkey':key,
           'ct':'2097152'
       }
       #下载
       r = requests.post(SearchUrl,headers=self.header,data=body)
       #配置下载后的
       r.encoding = 'gb2312'

       if r.ok:
           #print(len(r.text))

           html = etree.HTML(r.text)
          #获取小说名称并且比较是否符合
           novelTitle = html.xpath('//*/div[@id="info"]/h1/text()')[0]

           if novelTitle == novelName:
               novelUpdateTime = html.xpath('//div[@id="info"]/p[3]/text()')[0]

               novelUpdateTime = re.match('.*：(.*)', novelUpdateTime).group(1)

               novelAuthor = re.match('.*：(.*)',
                                html.xpath('//div[@id="info"]/p[1]/text()')[0]).group(1)
               novelLastestChapter = html.xpath('//div[@id="info"]/p[4]/a/text()')[0]
               novelLastestChapterURL = r.url + html.xpath('//div[@id="info"]/p[4]/a/@href')[0]
               self.novelMessage['novelTitle'] = novelTitle
               self.novelMessage['novelAuthor'] = novelAuthor
               self.novelMessage['novelUpdateTime'] = novelUpdateTime
               self.novelMessage['novelLastestChapter'] = novelLastestChapter
               self.novelMessage['novelLastestChapterURL'] = novelLastestChapterURL

              # print(novelTitle)
              # print(novelAuthor)
              # print(novelLastestChapter)
              # print(novelUpdateTime)
              #如果点击了获取详情
               if detail == True:
                   #获取所有的url和章节名称
                   self.totalChapterDict = self.GetTotalChapter(html)
           pass

       else:
           self.novelMessage = None
    def GetTxt(self):
        if len(self.txt)>0:
            return self.txt
        else:
            return None

    def EncodenovleName(self,novelName):
        return bytes(novelName,'gb2312')

   #获取小说的章节内容
    def GetNovel(self,url):
        r = requests.get(url,headers=self.header)
        r.encoding = 'gb2312'
        html = etree.HTML(r.text)
        contents = html.xpath('//div[@class="content_read"]//div[@id="content"]/text()')
        s = ''
        #返回是一个list，将所有内容合并起来，并且替换个别字符
        for i in contents:
            s += i
        self.txt = s.replace('\xa0', '')


    def GetLastestTxt(self):
        self.GetNovel(self.novelMessage['novelLastestChapterURL'])
        return self.txt



    def GetNovelMessage(self):
        return self.novelMessage

    def GetNovelTxt(self):
        return self.txt

   #获取小说的所有章节以及名称
    def GetTotalChapter(self,html):
       #获取了所有章节的list
        totalChapters = html.xpath('//div[@class="box_con"][2]//dl/dd')
        for num in range(0,len(totalChapters)):
            href = self.url + html.xpath('//div[@class="box_con"][2]//dl/dd')[num].xpath('a/@href')[0]
            title = html.xpath('//div[@class="box_con"][2]//dl/dd')[num].xpath('a/text()')[0]
            self.totalChapter[num]=[href,title]
            self.totalChapterList.append(href)
        pass

    def GetTotalChapterDict(self):
        return self.totalChapter

    def GetTotalChapterList(self):
        return self.totalChapterList


if __name__ == '__main__':
    #txt = biquge().GetTxt()
    print(biquge("我的一天有48小时",True).GetNovelMessage())