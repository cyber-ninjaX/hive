import os
import sys


SETTINGS_MODULE = 'hive.settings'
REPO_DIR = os.path.dirname(os.path.dirname(__file__))
APPS_DIR = os.path.join(REPO_DIR, 'apps')

# add the app code to the path
sys.path.append(REPO_DIR)  # project
sys.path.append(APPS_DIR)  # local apps

# set settings module and create wsgi app
os.environ['DJANGO_SETTINGS_MODULE'] = SETTINGS_MODULE
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# def debug_application(environ, start_response):
#     """Simple debug WSGI app."""
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     return ['Hello from hive!']
# application = debug_application
