import sys
sys.path.append("util")
sys.path.append("../..")
sys.path.append("..")
import os
from django.core.mail import *
from smthtop10.models import UserProfile
from datetime import date
today=date.today()
archive="./archive/"+today.strftime("%Y%m%d")+"/"

#gernarater mobi files
mobifile=archive+"sm.mobi"
htmlfile=archive+"sm.html"
kindlegen="./kindlegen"
os.system(kindlegen+" "+htmlfile)
print mobifile
if os.path.isfile(mobifile):
    t=EmailMessage()
    for i in UserProfile.objects.all():
        t.to.append(i.kindlemail)
    t.attach_file(mobifile)
    t.send()
