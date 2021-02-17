"""
WSGI config for drf-mongo-api drf-mongo-api.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangodrf-mongo-api.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf-mongo-api.settings')

application = get_wsgi_application()
