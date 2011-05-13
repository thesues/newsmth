from registration.forms import RegistrationForm
from forms import *
def user_created(sender, user, request, **kwargs):
    form = UserRegsiterForm(request.POST)
    profile=UserProfile(user=user)
    profile.kindlemail=form.data['kindlemail']
    profile.updateTime=form.data['updateTime']
    user.is_active=True
    user.save()
    profile.activation_key="ALREADY_ACTIVATED"
    profile.save()
from registration.signals import user_registered
user_registered.connect(user_created)
