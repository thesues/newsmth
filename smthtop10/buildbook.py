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
from django.template import Template
import cPickle 
from url_pic_finder import find_url
from datetime import date
from down_image import down_image

today=date.today()
smthurl=settings.SMTH_URL
smthorigurl="http://www.newsmth.net/bbscon.php"
ckpath="./"
userid="sea286"
userpass="zhu8jie"
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
                a.imagefilenameList.append(down_image(smth,imageurl))
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
        if(feed.numOfPosts==5):
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


sumaryFeeds.append(feed)
f=open("./testfeed","w")
cPickle.dump(sumaryFeeds,f)
f.close()
