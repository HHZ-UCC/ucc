import logging

from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder

from django.http import HttpResponse

from django.template.loader import render_to_string
from django.utils import timezone

import json

from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import RegistryService
# Create your views here.
import json

registry_service = RegistryService()
host = settings.HOST

@api_view(['POST'])
def bot_action(request):
    registered_apps = registry_service.get_registered_apps()
    response = render_to_string('cards/ac_registry_card.json', { 'host': host, "registered_apps" : registered_apps })
    return HttpResponse(response, content_type='application/json')