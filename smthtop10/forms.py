from registration.forms import RegistrationForm
from models import *
from django import forms

#this is for registration
class UserRegsiterForm(RegistrationForm):
    kindlemail=forms.EmailField()

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=["user"]
        
