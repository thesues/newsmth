import sys
sys.path.append("util")
sys.path.append("../..")
sys.path.append("..")
from smthapi import SimpleSMTH
from  smthparser import BeautyArticleProcessor
from smthparser import Top10Parser
import pdb
from django.template import Template, Context
from django.shortcuts import render_to_response
from django.conf import settings
from models import *
from bookTemplate import bookTemplate
import cPickle
 

f=open("./testfeed","r")
sumaryFeeds=cPickle.load(f)
f.close()
t=Template(bookTemplate)
c=Context({"sumaryFeeds":sumaryFeeds})
renderdHtml=t.render(c)
print renderdHtml.encode("utf8")
