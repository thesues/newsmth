# -*- coding: utf-8 -*-
import urllib
import re
import os
import urllib2
import httplib
import cookielib
import socket
#from django.conf import settings

ckpath="./"

class SimpleSMTH:
    def __init__(self):
        self.cj = cookielib.LWPCookieJar()
        
    def getCj(self):
        return self.cj
    def saveCj(self,key):
        self.cj.save(filename = ckpath+key+'.ck',ignore_discard=True, ignore_expires=True)
    
    def setCj(self,key):
#        try:
         self.cj.load(filename = ckpath+key+'.ck',ignore_discard=True, ignore_expires=True)
 #       except IOError:
 #           print 'ioe'
        
    def smthLogin(self,uid,psw):
#        self.cj = cookielib.CookieJar()
        post_data = urllib.urlencode({'id':uid,
		                              'passwd':psw,
		                              'kick_multi':1})
        path = 'http://www.newsmth.net/bbslogin.php/'
        try:
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
            opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]
            urllib2.install_opener(opener)
            req = urllib2.Request(path,post_data)
            conn = urllib2.urlopen(req)
            out = conn.read()
            if out.find('alert') > 0:
                return -1
            else:
                return 0
        except:
            print 'fail'
            return -1
 
    def get_url_data(self,url):
		#print "Get: ",url
        isOK = False
        try1 = 0
        try2 = 0
        while try1 < 5 and isOK == False:
            try:
                opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
                opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]
                urllib2.install_opener(opener)            
                req2 = urllib2.Request(url)
                htmlSource = urllib2.urlopen(req2).read()
#		        print htmlSource
            except:
                try2 = try2+1
            if try2 > try1:
                try1 = try2
            else:
                isOK = True

        if isOK:
            return htmlSource
        else:             
            return ""

    def post_url_data(self,url,data):
        isOK = False
        try1 = 0
        try2 = 0
        while try1 < 5 and isOK == False:
            try:
                opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
                opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]
                urllib2.install_opener(opener)            
                req2 = urllib2.Request(url,urllib.urlencode(data))
		        #req2 = urllib2.Request(url,data)
                htmlSource = urllib2.urlopen(req2).read()
            except:
                raise
                try2 = try2+1
            if try2 > try1:
                try1 = try2
            else:
                isOK = True

        if isOK:
            return htmlSource
        else:             
            return ""
        
