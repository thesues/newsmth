from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import login, logout
from registration.views import register
from smthtop10.forms import UserRegsiterForm
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^newsmth/', include('newsmth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^smthtop10/',include('smthtop10.urls')),
<<<<<<< HEAD
    (r'^accounts/',include('registration.urls'))
=======
    (r'^accounts/register$',register,{'form_class': UserRegsiterForm,'backend': 'registration.backends.default.DefaultBackend'}),
    (r'^accounts/', include('registration.backends.default.urls')),
>>>>>>> 98520ee0438aa2b469f9b168bdb479b64f93f0df
)
