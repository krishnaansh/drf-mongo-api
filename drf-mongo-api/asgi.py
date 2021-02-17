"""
ASGI config for drf-mongo-api drf-mongo-api.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangodrf-mongo-api.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf-mongo-api.settings')

application = get_asgi_application()
