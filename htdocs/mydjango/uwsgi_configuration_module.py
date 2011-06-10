#!/Applications/MNPP/Library/python26/bin/python
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mydjango.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

