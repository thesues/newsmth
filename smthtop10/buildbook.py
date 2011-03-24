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

smthurl=settings.SMTH_URL
ckpath="./"
userid="sea286"
userpass="zhu8jie"
def getContent(smth,parser,board,articleid,feed,next):
    if next==0:
        out=smth.get_url_data(smthurl+"?act=article&board="+board+"&id="+articleid)
        parser.reset()
        parser.feed(unicode(out,"gbk","ignore"))
        result=parser.getall()
        #to be contented
#        print result["c"]
#        pdb.set_trace()
        a=Post(author=result["a"],content=result["c"],signature=result["sign"],reference=result["ref"],attached=False)
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
        if(feed.numOfPosts==50):
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

    def down_image(self, url, referer=None, filename=None):
        """download image"""

        print "download: %s" % url,
        
        url = escape.utf8(url)
        image_guid = hashlib.sha1(url).hexdigest()

        x = url.split('.')
        ext = 'jpg'
        if len(x) > 1:
            ext = x[-1]

            if len(ext) > 4:
                ext = ext[0:3]

            ext = re.sub('[^a-zA-Z]','', ext)
            ext = ext.lower()

            if ext not in ['jpg', 'jpeg', 'gif','png','bmp']:
                ext = 'jpg'

        y = url.split('/')
        h = hashlib.sha1(str(y[2])).hexdigest()

        hash_dir = os.path.join(h[0:1], h[1:2])
        filename = image_guid + '.' + ext

        img_dir  = os.path.join(self.work_dir, 'data', 'images', hash_dir)
        fullname = os.path.join(img_dir, filename)
        
        localimage = 'images/%s/%s' % (hash_dir, filename)
        if os.path.isfile(fullname) is False:
            if not os.path.exists(img_dir):
                os.makedirs( img_dir )
            try:                
                req = urllib2.Request(url)
                req.add_header('User-Agent', self.user_agent)
                req.add_header('Accept-Language', 'zh-cn,zh;q=0.7,nd;q=0.3')

                if referer is not None:
                    req.add_header('Referer', referer)

                response = urllib2.urlopen(req)

                localFile = open(fullname, 'wb')
                localFile.write(response.read())

                response.close()
                localFile.close()
                print "done."
            except Exception, e:
                print 'fail: %s' % e
                localimage = False
            finally:
                localFile, response, req = None, None, None
        else:
            print "exists."
        
        return localimage


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
    #pdb.set_trace()
    getContent(smth,articleparser,article['b'],article['gid'],feed,0)
    getContent(smth,articleparser,article['b'],article['gid'],feed,1)
    print feed.title
    sumaryFeeds.append(feed)


f=open("./testfeed","w")
cPickle.dump(sumaryFeeds,f)
f.close()
