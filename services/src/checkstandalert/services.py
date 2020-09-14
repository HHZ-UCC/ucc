import requests
import json

from django.conf import settings
from django.utils import timezone
from django.template.loader import render_to_string

from base.models import Device

class AlertService:
    topic_name = "kassenalert"

    def on_message(self, message):
        try:
            print("value=%s" % ( message) )
            # TODO validate payload
            messagePayload = json.loads(message)
            devicePayload = messagePayload["device"]
            device, created = Device.objects.update_or_create(
                defaults={
                    'external_id': devicePayload["id"],
                    'type': devicePayload["deviceType"],
                    'location': devicePayload["ss_location"],
                    'created_at': timezone.now()
                }
            )
            # # TODO use description from Alert (ThingsBoard)
            # ticket = Ticket(description="Drucker patrone ausgegangen", status="offen", fk_device=device, created_at=timezone.now() )
            # ticket.save()
            
            host = settings.HOST
            payload = render_to_string('../templates/cards/checkstandalert.json', {'ticket': '', 'host' : host}).replace("\n", "")
            payload = json.dumps(json.loads(payload))
            requests.post(settings.BOT_SERVICE_URL, data=payload, headers={'Content-Type':'application/json'})
        except Exception as e:
            print("An exception occurred " + str(e))


# {
# 	"device": {
# 		"deviceType": "waage",
# 		"shared_location": "Obstabteilung",
# 		"id": "30080bb0-d513-11ea-8c9b-b1fb594c51a9",
# 		"deviceName": "Obstwaage"
# 	},
# 	"content": {
# 		"status": "ok",
# 		"cartridge": 50,
# 		"paper": 67
# 	}
# }