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
from smthtop10.forms import *
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

def main(request):
    threads=Thread.objects.all()
    return render_to_response("smthtop10/main.html",add_csrf(request,threads=threads))

@login_required
def profile(request,pk):
    profile=UserProfile.objects.get(user=pk)
    pf=ProfileForm(instance=profile)
    return render_to_response("smthtop10/profile.html",add_csrf(request,pf=pf))
   
def add_csrf(request,**kwargs):
    d=dict(user=request.user,**kwargs)
    d.update(csrf(request))
    return d
def help(request):
    return render_to_response("smthtop10/help.html",add_csrf(request))
