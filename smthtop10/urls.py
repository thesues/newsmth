from django.conf.urls.defaults import *
<<<<<<< HEAD
from smthtop10.models import *

urlpatterns = patterns('smthtop10.views',
                       (r"^$", "main"),
                       (r"^help$","help"),
                       (r"^profile/(\d+)$","profile"),
                     
)
=======
from django.conf import settings

urlpatterns= patterns("smthtop10.views",
(r"^$","main"),
(r"^profile/(\d)/$","profile"),
(r"^help$","help")
)

urlpatterns+=patterns("",
(r"^archive/(?P<path>.*)$","django.views.static.serve",{'document_root':settings.MEDIA_ROOT}),)
>>>>>>> 98520ee0438aa2b469f9b168bdb479b64f93f0df
