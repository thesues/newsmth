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
from smthtop10.models import *
from bookTemplate import bookTemplate
from django.template import Template
import cPickle 
from url_pic_finder import find_url
from datetime import date
from down_image import down_image
from bookTemplate import bookTemplate
from django.template import Template, Context
import os

today=date.today()
smthurl=settings.SMTH_URL
smthorigurl="http://www.newsmth.net/bbscon.php"
userid="sea286"
userpass="zhu8jie"
archive="./archive/"+today.strftime("%Y%m%d")+"/"
if os.path.isdir(archive):
    pass
else:
    os.mkdir(archive)

def getContent(smth,parser,board,articleid,feed,next):
    if next==0:
        out=smth.get_url_data(smthurl+"?act=article&board="+board+"&id="+articleid)
        parser.reset()
        parser.feed(unicode(out,"gbk","ignore"))
        result=parser.getall()
        if result["pic"]=="":
            a=Post(author=result["a"],content=result["c"],signature=result["sign"],reference=result["ref"],attached=False)
        else:
            origout=smth.get_url_data("http://www.newsmth.net/"+result["pic"])
            a=Post(author=result["a"],content=result["c"],signature=result["sign"],reference=result["ref"],attached=True)
            print find_url(origout)
            for imageurl in find_url(unicode(origout,"gbk")): 
                a.imagefilenameList.append(down_image(smth,imageurl,archive))
        feed.title=result['t']
        feed.append(a)
    elif next==1:
        out=smth.get_url_data(smthurl+"?act=article&board="+board+"&id="+articleid+"&p=tn")
        parser.reset()
        parser.feed(unicode(out,"gbk","ignore"))
        result=parser.getall()
        #print result["c"]
        a=Post(author=result["a"],content=result["c"],signature=result["sign"],reference=result["ref"],attached=False)
        feed.append(a)
        if(feed.numOfPosts==10):
            return
        #to be contented
        if result["id"]!=articleid:
            getContent(smth,parser,board,result["id"],feed,1)

def login(smth):
    r=smth.smthLogin(userid,userpass)
    if r==0:
        key=context.gen_sid()
        smth.saveCj(key)
    else:
        print "login error"



smth = SimpleSMTH()
sumaryFeeds=[]
feed=Feed()
login(smth)
#get top10 topics
out=smth.get_url_data("http://www.newsmth.net/rssi.php?h=1")
top10parser=Top10Parser(out)
articleparser=BeautyArticleProcessor()
for article in top10parser.getall():
    feed=Feed()
    getContent(smth,articleparser,article['b'],article['gid'],feed,0)
    getContent(smth,articleparser,article['b'],article['gid'],feed,1)
    print feed.title
    sumaryFeeds.append(feed)

#write data
f=open(archive+"/sm.data","w")
cPickle.dump(sumaryFeeds,f)
f.close()

#write to html
t=Template(bookTemplate)
c=Context({"sumaryFeeds":sumaryFeeds})
renderdHtml=t.render(c)
f=open(archive+"/sm.html","w")
f.write(renderdHtml.encode("utf8"))
f.close()
#write to datebases
p=Thread(date=today,location=archive+"/sm.html",mobiLocation=archive+"/sm.mobi")
p.save()
