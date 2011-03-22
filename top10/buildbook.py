import sys
sys.path.append("util")
sys.path.append("../..")
sys.path.append("..")
import mcconns as context
from smthapi import SimpleSMTH
from  smthparser import BeautyArticleProcessor
from smthparser import Top10Parser
import pdb
import sys
from django.template.context import RequestContext
from django.template import loader, Context
from django.shortcuts import render_to_response
from django.conf import settings
from models import *
from bookTemplate import bookTemplate

smthurl=settings.SMTH_URL
sumaryFeeds=[]
feed=[]
def getContent(smth,parser,board,articleid,feed,next):
    if next==0:
        out=smth.get_url_data(smthurl+"?act=article&board="+board+"&id="+articleid)
        parser.feed(unicode(out,"gbk","ignore"))
        result=parser.getall()
        #to be contented
#        print result["c"]
#        pdb.set_trace()
        a=Post(author=result["a"],content=result["c"],attached=False,title=result['t'])
        feed.append(a)
    elif next==1:
        out=smth.get_url_data(smthurl+"?act=article&board="+board+"&id="+articleid+"&p=tn")
        parser.reset()
        parser.feed(unicode(out,"gbk","ignore"))
        result=parser.getall()
        #print result["c"]
        a=Post(author=result["a"],content=result["c"],attached=False,title=result['t'])
        feed.append(a)
        #to be contented
        if result["id"]!=articleid:
            getContent(smth,parser,board,result["id"],feed,1)

smth = SimpleSMTH()
#login(smth)
#get top10 topics
out=smth.get_url_data("http://www.newsmth.net/rssi.php?h=1")
top10parser=Top10Parser(out)
articleparser=BeautyArticleProcessor()
#for article in top10parser.getall():
#    getContent(smth,articleparser,article['b'],article['gid'],feed,0)
#    getContent(smth,articleparser,article['b'],article['gid'],feed,1)
getContent(smth,articleparser,"LinuxDev","252618",feed,0)
getContent(smth,articleparser,"LinuxDev","252618",feed,1)
sumaryFeeds.append(feed)
a=feed[:]
a[1].title="this is a test"
sumaryFeeds.append(a)
#render to html

t=Template(bookTemplate)
c=Context("sumaryFeeds":sumaryFeeds)
renderdHtml=t.render(c)   
