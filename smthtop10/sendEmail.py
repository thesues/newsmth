import sys
sys.path.append("..")
sys.path.append("../..")
from smthtop10.models import UserProfile
from django.core import mail
messages=[]
t=mail.EmailMessage()
for i in UserProfile.objects.all():
    t.to.append(i.kindlemail)
    print i.kindlemail
t.from_email="admin@pushkindle.com"
t.attach_file("/home/zhangdongmao/newsmth/smthtop10/archive/20110331/sm.mobi")
messages.append(t)
connection = mail.get_connection()
connection.open()
connection.send_messages(messages)
connection.close()
