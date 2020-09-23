from django.apps import AppConfig
from django.apps import apps
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class RegistryConfig(AppConfig):
    name = 'registry'