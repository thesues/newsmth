from smthparser import BeautyArticleProcessor
from smthapi import SimpleSMTH
from url_pic_finder import *



smth=SimpleSMTH()
out=smth.get_url_data("http://www.newsmth.net/atomic.php?act=article&board=Picture&id=569616")
parser=BeautyArticleProcessor()
parser.feed(unicode(out,"gbk","ignore"))
result=parser.getall()
print "==================="
print result['c']
print "==================="
print result['ref']
print "==================="
print result['sign']
print "==================="
urls="http://www.newsmth.net/bbscon.php"+result['pic']
print find_url(urls)

