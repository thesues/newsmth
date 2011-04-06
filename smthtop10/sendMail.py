import sys
sys.path.append("util")
sys.path.append("../..")
sys.path.append("..")
from django.core.mail import *
from smthtop10.models import UserProfile
t=EmailMessage()
for i in UserProfile.objects.all():
    t.to.append(i.kindlemail)
t.attach_file("/home/zhangdongmao/newsmth/smthtop10/archive/20110405/sm.mobi")
t.send()

