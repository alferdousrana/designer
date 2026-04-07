import os
import sys

path = '/home/alrana/designer/server'
os.chdir(path)

if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
