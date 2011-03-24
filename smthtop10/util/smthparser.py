# # -*- coding: utf-8 -*-  
from HTMLParser import HTMLParser
from xml.dom import minidom

class FavProcessor(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.in_a = 0
        self.boardurl = []
        self.boards = []
    

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            href = [v for k, v in attrs if k=='href']
            if href[0].find('act=board')>0:
                self.in_a=1
                self.boardurl.append(href[0])


    def handle_endtag(self, tag):
        if tag == 'a':
            if self.in_a==1:
                self.in_a=0


    def handle_data(self,data):
        if self.in_a==1:
            self.boards.append(data)
            
            
    def getfav(self):
        result = []
        i =0
        for v in self.boards:
            pare={}
            pare[v] = self.boardurl[i]
            i=i+1
            result.append(pare)
        return result
       
class BoardProcessor(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.threads = []
        self.btag = 0
        self.linkTag = 0
        self.tcount = 0
        self.preinfo = ""
        self.ppage = 0
        self.npage = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'br': #will be thread info next
            self.btag = 1
        if tag == 'a':
            if self.btag == 1:
                self.btag =0           
            href = [v for k, v in attrs if k=='href']
            url = href[0]
            idpos = url.find('id=')
            if idpos >0:
                self.linkTag =1
                threadId = url[idpos+3:len(url)]
                thread = {}
                thread['id'] = threadId
                thread['info'] = self.preinfo
                self.threads.append(thread)
            pagetag = url.find('page=')
            if pagetag > 0:
                if self.ppage!=0 and self.ppage!=1:
                    self.npage = int(url[pagetag+5:len(url)])
                else:
                    self.ppage = int(url[pagetag+5:len(url)])
                
    def handle_data(self,data):
#        utfdata = data.decode("gb2312").encode("utf8")
        utfdata = data
        if self.linkTag==1:
            thread = self.threads[self.tcount]
            thread ['title'] = utfdata
        if self.btag==1:
            self.preinfo = utfdata

    def handle_endtag(self, tag):
        if tag == 'a':
            if self.linkTag==1:
                self.linkTag=0
                self.tcount = self.tcount +1
       
    def showboard(self):
        return self.threads
    
    def getppage(self):
        return self.ppage
    
    def getnpage(self):
        return self.npage


class TopicProcessor():
    def __init__(self,content):
        self.threadList = []
        import StringIO
        self.contentStream = StringIO.StringIO(content)
        self.page = 0
        
    def getall(self):
        i = 0
        for line in self.contentStream.readlines():
            i = i+1
            if i == 21: #get page
                parser = line.split(',')
                self.page = int(parser[5])
            elif line.startswith('c.o'): #get one thread
                parser = line.split(',')
                thread = {}
                thread['id'] = parser[1]
                thread['a'] = parser[2][1:-1]
                thread['d'] = parser[4]
                thread['t'] = parser[5][1:-1]
                self.threadList.append(thread)
        self.contentStream.close()
        return self.threadList
    
    def getpage(self):
        return self.page              


class ArticleProcessor(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.content = ""
        self.btag = 0
        self.count =0
        self.acount =0
        self.hasTag =0
        self.title = ''
        self.topid = 0
        self.aid = 0
                
    def handle_data(self,data):
        if self.btag==1:
            self.count = self.count+1
#            print unicode(data,"gbk")+',count'+str(self.count)+',len='+str(len(data))
            if self.count == 3:
                head = data.split(':')
                self.title = ''.join(v for v in head[1::])
#                print unicode(head[1],"gbk")
            if self.hasTag == 1:
                self.content=self.content+"\n"+data
            else:
                self.content=self.content+data
        self.hasTag = 0
        
    def handle_endtag(self, tag):
        if tag == 'p':
            self.btag = 1
        if tag == 'body':
            self.btag = 0

    def handle_starttag(self, tag, attrs):
        self.hasTag = 1
        if tag == 'a':
            self.acount = self.acount + 1
            if self.acount == 2:
                href = [v for k, v in attrs if k=='href']
                url = href[0]
                print url
                idpos = url.find('id=')
                self.topid = url[idpos+3:len(url)]
            if self.acount == 1:
                href = [v for k, v in attrs if k=='href']
                url = href[0]
                print url
                idpos = url.find('id=')
                self.aid = url[idpos+3:len(url)]

                      
                            
    def show(self):
        return self.content
        
    def gettitle(self):
        return self.title

    def gettopid(self):
        return self.topid
    def getid(self):
        return self.aid


class BeautyArticleProcessor(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.content = ""
        self.signature=""
        self.reference=""
        self.btag = 0
        self.count =0
        self.acount =0
        self.hasTag =0
        self.title = ''
        self.topid = 0
        self.aid = 0
        self.author = ''
        self.date = ''
        self.space = 0
        self.contentTag=0
        self.signTag=0
        self.refTag=0
    def reset(self):
        HTMLParser.reset(self)
        self.content = ""
        self.signature=""
        self.reference=""
        self.btag = 0
        self.count =0
        self.acount =0
        self.hasTag =0
        self.title = ''
        self.topid = 0
        self.aid = 0
        self.author = ''
        self.date = ''
        self.space = 0
        self.contentTag=0
        self.signTag=0
        self.refTag=0
                
    def handle_data(self,data):
        if self.btag==1:
            if self.space!=1:
                self.count = self.count+1
#            print unicode(data,"gbk")+',count'+str(self.count)+',len='+str(len(data))
            if self.count == 1:
                p1 =data.find(':')
                p2 = data.find(',')
                self.author = data[p1+2:p2]
            if self.count == 3:
                headpos = data.find(':')
                self.title = data[headpos+2:len(data)]
            if self.count == 4:
                if self.space != 1:
                    p1 = data.find('(')
                    p2 = data.find(')')
                    self.date = data[p1+1:p2]
                else:
                    p2 = data.find(')')
                    self.date = self.date +" "+data[:p2]
                    self.space = 0
            if self.count == 5:
                 self.hasTag = 1
            if self.hasTag == 1:
                if data.startswith(u"【"):
                    self.refTag=1
                if data.startswith("--"):
                    self.refTag=0
                    self.signTag=1
                if self.refTag==1:
                    self.reference=self.reference+data+'\n'
                elif self.signTag==1:
                    if data.startswith(u"※"):
                        return
                    self.signature=self.signature+data+'\n'
                else:
                    self.content=self.content+data+'\n'
#            else:
#                self.content=self.content+data
#        self.hasTag = 0
    
    def handle_entityref(self, entity):
        if self.count == 4:
            if entity == "nbsp":
                print "recv space"
                self.space = 1
            
    
    def handle_endtag(self, tag):
        if tag == 'p':
            self.btag = 1
        if tag == 'body':
            self.btag = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.acount = self.acount + 1
            if self.acount == 2:
                href = [v for k, v in attrs if k=='href']
                url = href[0]
                print url
                idpos = url.find('id=')
                self.topid = url[idpos+3:len(url)]
            if self.acount == 1:
                href = [v for k, v in attrs if k=='href']
                url = href[0]
                print url
                idpos = url.find('id=')
                self.aid = url[idpos+3:len(url)-5]

    def getall(self):
        result = {}
        result['a'] = self.author
#        print self.author
        result['t'] = self.title
#        print self.title
        result['d'] = self.date
#        print self.date
        result['c'] = self.content
#        print self.content
        result['id'] = self.aid
        result['tid'] = self.topid
        result['ref']=self.reference
        result['sign']=self.signature
        return result
                            
    def show(self):
        return self.content
        
    def gettitle(self):
        return self.title

    def gettopid(self):
        return self.topid
    def getid(self):
        return self.aid

class Top10Parser():
    def __init__(self,xmldata):
        self.threadList = []
        import StringIO
        self.xmldata = StringIO.StringIO(xmldata)

    def getall(self):
        xmldoc = minidom.parse(self.xmldata)
        itemlist= xmldoc.getElementsByTagName('item')
        for item in itemlist:
            one = {}
            one['t'] = item.getElementsByTagName('title')[0].firstChild.data
            url = item.getElementsByTagName('link')[0].firstChild.data
            gpos = url.find('gid=')
            bpos = url.find('board=')
            one['gid'] = url[gpos+4:len(url)]
            one['b'] = url[bpos+6:gpos-1]
            one['a'] = item.getElementsByTagName('author')[0].firstChild.data
            one['d'] = item.getElementsByTagName('pubDate')[0].firstChild.data
            self.threadList.append(one)
        return self.threadList
