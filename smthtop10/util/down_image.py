from url_pic_finder import *
from smthapi import SimpleSMTH
import hashlib
import urllib2
import sys
import Image
from cStringIO import StringIO
def down_image(smth,url):
    print "download image from :%s"%url
    image_uid=hashlib.md5(url).hexdigest()
    y=url.split("/")[2]
    filename=image_uid+'.'+'jpg'
    localimage='images/%s' % filename
    imageData=smth.get_url_data(url)
    im=Image.open(StringIO(imageData)).convert("L")
    #resize
    width,height=im.size
    im2=im.resize((width/2,height/2),Image.ANTIALIAS)
    im2.save(localimage)
    return localimage
    
if __name__=="__main__":
    url="http://www.newsmth.net/bbscon.php?bid=382&id=570506"
    smth=SimpleSMTH()
    out=smth.get_url_data(url)
    for imageurl in find_url(unicode(out,"gbk")):
        print down_image(smth,imageurl)

