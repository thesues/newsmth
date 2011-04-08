import sys
sys.path.append("util")
sys.path.append("../..")
sys.path.append("..")
from smthapi import SimpleSMTH
from  smthparser import BeautyArticleProcessor
from smthparser import Top10Parser
import pdb
from django.template import Template, Context
from django.conf import settings
from bookTemplate import bookTemplate
import cPickle
import re
from datetime import date

today=date.today()

dataarchive="./archive/"+today.strftime("%Y%m%d")+"/sm.data"
f=open(dataarchive,"r")
sumaryFeeds=cPickle.load(f)
f.close()

t=Template(bookTemplate)
c=Context({"sumaryFeeds":sumaryFeeds})
renderdHtml=t.render(c)
print renderdHtml.encode("utf8")
