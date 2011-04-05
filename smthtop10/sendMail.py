import sys
sys.path.append("util")
sys.path.append("../..")
sys.path.append("..")
from django.core.mail import *
t=EmailMessage()
t.attach_file("/home/zhangdongmao/newsmth/smthtop10/archive/20110405/sm.mobi")
t.to=["deanraccoon@free.kindle.com"]
t.send()

