"""
WSGI config for aecc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

ENVIRONMENT = os.getenv('ENVIRONMENT', 'DEVELOPMENT').title()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aecc.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', ENVIRONMENT)

from configurations.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
