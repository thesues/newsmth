# Create your views here.
import sys
import pdb
sys.path.append("/home/zhangdongmao/newsmth/smthtop10/util")
import mcconns as context
from smthapi import SimpleSMTH
from  smthparser import BeautyArticleProcessor
from smthparser import Top10Parser
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from smthtop10.models import *

def main(request):
    return render_to_response("smthtop10/main.html")

