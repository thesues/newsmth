from registration.forms import RegistrationForm
from models import *
from django import forms
from registration.signals import user_registered
import pdb

#this is for registration
class UserRegsiterForm(RegistrationForm):
    kindlemail=forms.EmailField()

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
def user_created(sender, user, request, **kwargs):
    form = UserRegsiterForm(request.POST)
    pdb.set_trace()
    profile=UserProfile(user=user)
    profile.kindlemail=form.data['kindlemail']
    profile.save()
user_registered.connect(user_created)
