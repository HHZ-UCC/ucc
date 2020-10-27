import sys
import time

from django.apps import AppConfig
from django.conf import settings
import json

# import the logging library
import logging
import threading

from datetime import datetime
from kafka import KafkaConsumer

# Get an instance of a logger
logger = logging.getLogger(__name__)

class MaintenanceConfig(AppConfig):
    name = 'maintenance'
       
    @classmethod
    def consumer(cls): 
        while True:
            try: 
                from maintenance.services import TicketsService
                ticketService = TicketsService()
                kafkaConsumer = KafkaConsumer(
                    ticketService.topic_name,
                    # bootstrap_servers=settings.KAFKA_SERVERS,
                    bootstrap_servers='kafka:9093',
                    auto_offset_reset='latest',
                    # consumer_timeout_ms=500
                )
                for message in kafkaConsumer:
                    request_body = message.value.decode('utf-8')
                    ticketService.on_message(request_body)
                logger.info('Kafka consumer  for app %s started.', __name__)
            except:
                exception = sys.exc_info()[0]
                logger.info('Failed to start Kafka consumer with error %s', exception)
                time.sleep(10)
                logger.info('Retrying Kafka consumer for app %s', __name__)
                pass
            else:
                break

    @classmethod
    def start_consumer(cls):
        threading.Thread(target=self.consumer).start()

    def get_registry_info(self):
        host = settings.HOST
        return  {
            "app"         : self.verbose_name,
            "type"        : "list_tickets",
            "displayText" : "Zeige alle Tickets",
            "targetUrl"  : '{host}/services/{name}/bot/list_tickets'.format(host=host, name=self.name)
        }

 