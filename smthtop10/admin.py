from smthtop10.models import *
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    list_display=["user","kindlemail"]
admin.site.register(UserProfile,UserProfileAdmin)
