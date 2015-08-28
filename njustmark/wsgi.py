"""
WSGI config for bzsystem project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""


import sys
import os

djangopath = "C:/Python27/Lib/site-packages/django/bin"  
if djangopath not in sys.path:  
    sys.path.append(djangopath)

projectpath = 'C:/working/njustmark/'  
if projectpath not in sys.path:  
    sys.path.append(projectpath)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "njustmark.settings")



from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
