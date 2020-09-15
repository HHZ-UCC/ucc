from django.apps import AppConfig
from django.conf import settings

# import the logging library
import logging
import threading

from datetime import datetime
from kafka import KafkaConsumer

# Get an instance of a logger
logger = logging.getLogger(__name__)

class CheckstandalertConfig(AppConfig):
    name = 'checkstandalert'

    def ready(self):
        if settings.ENABLE_KAFKA_CONSUMER:
            threading.Thread(target=self.consumer).start()
    
    def consumer(self):
        logger.info('Starting kafka consumer for app %s', __name__)
        from checkstandalert.services import AlertService
        alertService = AlertService()
        kafkaConsumer = KafkaConsumer(
            'kassenalert',
            # bootstrap_servers=settings.KAFKA_SERVERS,
            bootstrap_servers='kafka:9093',
            auto_offset_reset='latest',
            # consumer_timeout_ms=500
        )
        for message in kafkaConsumer:
            request_body = message.value.decode('utf-8')
            alertService.on_message(request_body)

    def get_registry_info(self):
        host = settings.HOST
        return  {
            "app"         : self.verbose_name,
            "type"        : "list_alerts",
            "displayText" : "Zeige alle Alerts",
            "targetUrl"  : '{host}/services/{name}/bot/list_alerts'.format(host=host, name=self.name)
        }