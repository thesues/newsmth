import sys
sys.path.append("..")
sys.path.append("../..")
from smthtop10.models import UserProfile
from django.core import mail
t=mail.EmailMessage()
for i in UserProfile.objects.all():
    t.to.append("deanraccoon@kindle.com")
print t.to
t.from_email="admin@localhost"
t.subject="Convert"
t.body="sm.mobi"
t.attach_file("/home/zhangdongmao/newsmth/smthtop10/archive/20110331/sm.mobi")
t.send()

