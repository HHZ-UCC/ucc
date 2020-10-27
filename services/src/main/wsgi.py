"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings
from checkstandalert.apps import CheckstandalertConfig
from maintenance.apps import MaintenanceConfig

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)

if settings.ENABLE_KAFKA_CONSUMER:
    CheckstandalertConfig.start_consumer()
    MaintenanceConfig.start_consumer()