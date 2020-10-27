import logging

from django.conf import settings
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.template.loader import render_to_string

from .services import RegistryService

registry_service = RegistryService()
host = settings.HOST

@api_view(['POST'])
def bot_action(request):
    registered_apps = registry_service.get_registered_apps()
    response = render_to_string('cards/ac_registry_card.json', { 'host': host, "registered_apps" : registered_apps })
    return HttpResponse(response, content_type='application/json')