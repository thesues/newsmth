from registration.forms import RegistrationFormUniqueEmail
from models import *
from django import forms
from django.utils.translation import ugettext_lazy as _


#this is for registration
class UserRegsiterForm(RegistrationFormUniqueEmail):
    kindlemail=forms.EmailField(label=_("kindlemail"))
    updatetime=forms.ChoiceField(choices=UPDATE_TIME,label=_("updatetime"))
    def clean_kindlemail(self):
        if UserProfile.objects.filter(kindlemail=self.cleaned_data['kindlemail']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['kindlemail']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=["user"]


