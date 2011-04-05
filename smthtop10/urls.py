from django.conf.urls.defaults import *
from smthtop10.models import *

urlpatterns = patterns('smthtop10.views',
                       (r"^$", "main"),
                       (r"^help$","help"),
                       (r"^profile/(\d+)$","profile"),
                     
)
