import requests
import json

from django.conf import settings
from django.utils import timezone
from django.template.loader import render_to_string

from .models import Alert

host = settings.HOST

class AlertService:
    topic_name = "kassen_alert"

    def on_message(self, message):
        try:
            print("value=%s" % ( message) )

            alert = Alert(description="Bitte Kassenfrage akzeptieren.", status="offen", created_at=timezone.now() )
            payload = render_to_string('../templates/cards/notification/checkstandalert.json', {'alert': alert, 'host' : host}).replace("\n", "")
            payload = json.dumps(json.loads(payload))
            requests.post(settings.BOT_SERVICE_URL, data=payload, headers={'Content-Type':'application/json'})
        except Exception as e:
            print("An exception occurred " + str(e))