#!/usr/bin/env python
#coding=utf8
#appStore评论抓取

'''Author:glove
Date:2014.04.01'''

import urllib2
import re
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup

from htmlspecialchars_decode import htmlspecialchars_decode

id = '448165862'
for page in range(1, 2):
    comment_url_appstore='http://itunes.apple.com/cn/rss/customerreviews/id='+id+'/sortBy=mostRecent/page='+str(page)+'/xml'

    data_xml = htmlspecialchars_decode(urllib2.urlopen(comment_url_appstore).read())
    #soup = BeautifulSoup(data_xml)
    soup = BeautifulStoneSoup(data_xml)

    data = []
    data_font = soup.findAll('font')
    for data_font_single in data_font:
        data_br = data_font_single.find('br')
        if data_br != None:
            pattern = re.compile(r'<br>(.*)</br>')
            data_br = str(data_br)
            data_str = pattern.match(data_br).groups()[0]
            data.append(data_str)
            print data_str
#print data



