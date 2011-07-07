import os
import sys
import os.path
PROJECTDIR=os.path.abspath(os.path.dirname(__file__))
print PROJECTDIR
sys.path.append(PROJECTDIR)
sys.path.append(os.path.join(PROJECTDIR,'..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'newsmth.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
