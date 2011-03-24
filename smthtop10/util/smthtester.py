#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mcconns as context
import smthapi
import smthparser
userid="sea286"
userpass="zhu8jie"
smth = smthapi.SimpleSMTH()
r=smth.smthlogin(userid,userpass)
if r==0:
    key=context.gen_side()
    smth.saveCj(key)
out=smth.get_url_data('http://www.newsmth.net/atomic.php?act=article&board=Movie&id=&p=tn')
processor = smthparser.BeautyArticleProcessor()
processor.feed(unicode(out,"gbk"))
result=processor.getall()
print result['a']
print result['c']
processor.close()
#processor = smthparser.TopicProcessor(unicode(out,"gbk"))
#print processor.getall()
#print 'posting'
#out=smth.post_url_data('http://www.newsmth.net/atomic.php?act=post&board=Test&reid=0&post=1',{'text': u'\u6d4b\u8bd5'.encode#('gbk'), 'title': u'\u6d4b\u8bd5'.encode('gbk')})
#print unicode(out,"gbk")
#out=smth.get_url_data('http://www.newsmth.net/rssi.php?h=1')
#print out
#parser = smthparser.Top10Parser(out)
#print parser.getall()
