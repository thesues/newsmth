from django.conf.urls.defaults import *
from django.conf import settings
from smthtop10.views import *

urlpatterns= patterns("smthtop10.views",
                      url(r"^$",
                          main,
                          name="smthtop10_main"),
                      url(r"^profile/(\d+)/$",
                          profile,
                          name="smthtop10_profile"),
                      url(r"^help/$",
                          help,
                          name="smthtop10_help"),
                      url(r"^delete/(\d+)/$",
                          deleteUser,
                          name="smthtop10_delete")
)

#urlpatterns+=patterns("",
#(r"^archive/(?P<path>.*)$","django.views.static.serve",{'document_root':settings.MEDIA_ROOT}),)
