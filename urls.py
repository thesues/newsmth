from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import login, logout
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
    (r'^accounts/',include('registration.urls'))
)
