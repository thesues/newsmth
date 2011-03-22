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
 

f=open("./newtestfeed","r")
sumaryFeeds=cPickle.load(f)
f.close()
t=Template(bookTemplate)
c=Context({"sumaryFeeds":sumaryFeeds})
renderdHtml=t.render(c)
print renderdHtml.encode("utf8")
