from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns= patterns("smthtop10.views",
(r"^$","main"),
(r"^profile/(\d)/$","profile"),
(r"^help$","help")
)

urlpatterns+=patterns("",
(r"^archive/(?P<path>.*)$","django.views.static.serve",{'document_root':settings.MEDIA_ROOT}),)
