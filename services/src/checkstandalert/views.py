import logging

from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings

from django.http import HttpResponse

from django.template.loader import render_to_string
from django.utils import timezone

import json

from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response



from .models import Alert
from base.models import Device, Employee
from .services import AlertService

# Create your views here.
logger = logging.getLogger(__name__)
host = settings.HOST

@api_view(['POST'])
def assign_alert(request):
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
        Alert.objects.filter(pk=payload["alertId"]).update(fk_employee=employee)
        response = render_to_string('cards/alert_assigned.json', {'host': host, 'employee': employee})
        return HttpResponse(response, content_type='application/json')
    else:
       return Response(valid_ser.errors)

@api_view(['POST'])
def list_alerts(request): 
    alerts = Alert.objects.all()
    response = render_to_string('cards/list_alerts.json', {'host': host, 'alerts' : alerts})
    return HttpResponse(response, content_type='application/json')

@api_view(['GET'])
def notification(request): 
    alertService = AlertService()
    alertService.on_message({})
    return Response(status=status.HTTP_200_OK)

class PayloadValidator(serializers.Serializer):
    alertId = serializers.CharField(required=True, max_length=250)
    type = serializers.CharField(required=True, max_length=50)

class UserValidator(serializers.Serializer):
    id = serializers.CharField(required=True, max_length=250)    
    name = serializers.CharField(required=True, max_length=250)

class BotActionValidator(serializers.Serializer):
    payload = PayloadValidator()
    user = UserValidator()



# @api_view(['GET'])
# def test(request):
#     data = """{
#         "device": {
#             "deviceType": "waage",
#             "shared_location": "Obstabteilung",
#             "id": "30080bb0-d513-11ea-8c9b-b1fb594c51a9",
#             "deviceName": "Obstwaage"
#         },
#         "content": {
#             "status": "ok",
#             "cartridge": 50,
#             "paper": 67
#         }
#     }"""
    
#     messagePayload = json.loads(data)
#     devicePayload = messagePayload["device"]
#     device, created = Device.objects.update_or_create(
#         defaults={
#             'external_id': devicePayload["id"],
#             'type': devicePayload["deviceType"],
#             'location': devicePayload["shared_location"],
#             'created_at': timezone.now()
#         }
#     )
    
#     ticket = Ticket(description="Drucker patrone ausgegangen", status="offen", fk_device=device, created_at=timezone.now() )
#     ticket.save()
#     return Response(status=status.HTTP_200_OK)

