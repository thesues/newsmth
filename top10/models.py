from django.db import models

# Create your models here.
class Post():
    def __init__(self,author="unknow",title="unkown",content="unknow",attached=False):
        self.title=title
        self.author=author
        self.content=content
        self.attached=attached
    def __str__(self):
        return "%s:%s" % (self.author.encode("utf8"),self.content.encode("utf8"))
        
