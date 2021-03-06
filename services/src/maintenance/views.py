import logging

from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder

from django.http import HttpResponse

from django.template.loader import render_to_string
from django.utils import timezone
from django.conf import settings

import json

from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Ticket
from .services import TicketsService
from base.models import Device, Employee

# Create your views here.
logger = logging.getLogger(__name__)
host = settings.HOST
   
@api_view(['POST'])
def assign_ticket(request):
    valid_ser = BotActionValidator(data=request.data)
    if valid_ser.is_valid():
        request_body = valid_ser.validated_data
        user = request_body['user']
        payload = request_body['payload']
        
        employee, created = Employee.objects.update_or_create(
            defaults={
                'external_id': user["id"],
                'lastname': user["name"],
                'surname': user["name"],
            }
        )
        
        Ticket.objects.filter(pk=payload["ticketId"]).update(fk_employee=employee)
        response = render_to_string('cards/ticket_assigned.json', {'host': host, 'employee': employee})
        return HttpResponse(response, content_type='application/json')
    else:
       return Response(valid_ser.errors)


@api_view(['POST'])
def list_tickets(request): 
    tickets = Ticket.objects.all()
    response = render_to_string('cards/list_tickets.json', {'host': host, 'tickets' : tickets})
    return HttpResponse(response, content_type='application/json')


class PayloadValidator(serializers.Serializer):
    deviceId = serializers.CharField(required=True, max_length=250)
    ticketId = serializers.CharField(required=True, max_length=250)
    type = serializers.CharField(required=True, max_length=50)

class UserValidator(serializers.Serializer):
    id = serializers.CharField(required=True, max_length=250)    
    name = serializers.CharField(required=True, max_length=250)

class BotActionValidator(serializers.Serializer):
    payload = PayloadValidator()
    user = UserValidator()