from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Post():
    def __init__(self,author="unknow",content="unknow",signature="unknown",reference="unknown",attached=False):
        self.author=author
        self.content=content
        self.attached=attached
        self.signature=signature
        self.reference=reference
        self.imagefilenameList=[]
    def __str__(self):
        return "%s:\n%s" % (self.author.encode("utf8"),self.content.encode("utf8"))
        
class Feed():
    def __init__(self,title="unknown"):
        self.list=list()
        self.title=title
        self.numOfPosts=0
    def append(self,post):
        self.list.append(post)
        self.numOfPosts=self.numOfPosts+1
    def __str__(self):
        return self.title.encode("utf8")

class UserProfile(models.Model): 
    kindlemail=models.EmailField(max_length=75)
    user=models.ForeignKey(User,unique=True)
    def __unicode__(self):
        return unicode(self.user.username)

class Thread(models.Model):
    date=models.DateField(auto_now_add=True)
    location=models.FilePathField(path=None)
    mobiLocation=models.FilePathField(path=None)




