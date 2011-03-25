import urllib2
import pdb
import re
class picture_url():
    def __init__(self,sec1,sec2,sec3):
        self.sec1=sec1
        self.sec2=sec2
        self.sec3=sec3
    def build_url(self):
        return "http://att.newsmth.net/att.php?p.%s.%s.%s.jpg" % (self.sec1,self.sec2,self.sec3)

def find_url(out):
    #find prefix of jpg
    picture_url_array=[]
    pattern=re.compile(".*attWriter\((\d+),(\d+).*")
    obj=re.search(pattern,out)
    if obj!=None and obj.group(1)!=None and obj.group(2)!=None:
        sec1=obj.group(1)
        sec2=obj.group(2)
    else:
        return []
    array=re.findall("attach\(\S+, \S+, (\d+)\)",out)
    if len(array)!=0:
        for i in array:
            picture_url_array.append(picture_url(sec1,sec2,i).build_url())
    return picture_url_array
if __name__=="__main__":
    url="http://www.newsmth.net/bbscon.php?bid=382&id=569616"
    url1="http://www.newsmth.net/bbscon.php?bid=382&id=570506"
    url2="http://www.newsmth.net/bbscon.php?bid=382&id=570755"
    out=urllib2.urlopen(url).read()
    print find_url(unicode(out,"gbk"))
    out=urllib2.urlopen(url1).read()
    print find_url(unicode(out,"gbk"))
    out=urllib2.urlopen(url2).read()
    print find_url(unicode(out,"gbk"))
    
