"""
WSGI config for typeidea project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.get('PROFILE', 'dev')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'typeidea.settings.{profile}')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea.settings')

application = get_wsgi_application()
