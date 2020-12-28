from cabot.cabotapp.alert import AlertPlugin
from kafka_service import KafkaService
from os import environ as env
import json

from logging import getLogger
logger = getLogger(__name__)

class KafkaAlert(AlertPlugin):
    name = "Kafka"
    slug = "cabot_alert_twilio"
    author = "Hung Pham"
    version = "0.2.0"

    def send_alert(self, service, users, duty_officers):
        KafkaAlert.send_alert(self,service)
        return True
    def send_kafka(self, messageDto):
        BOOTSTRAP_SERVER =env.get('BOOTSTRAP_SERVER')
        ALERT_TOPIC =env.get('ALERT_TOPIC')
        message = json.dumps(messageDto.__dict__).encode()

        # Call produce function to send message to topic
        KafkaService.produceMessage(KafkaService,BOOTSTRAP_SERVER,ALERT_TOPIC,message)
        logger.info('Sent to kafka successfuly')

