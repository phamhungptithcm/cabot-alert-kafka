from kafka_service import KafkaService
from os import environ as env
import json
from cabot.cabotapp.alert import AlertPlugin

class KafkaAlert(AlertPlugin):
    BOOTSTRAP_SERVER = ''
    ALERT_TOPIC=''
    NUM_PARTITIION = 1
    REPLICATION_FACTOR= 1
    def __init__(self):
        KafkaAlert.BOOTSTRAP_SERVER = env.get('BOOTSTRAP_SERVER')
        KafkaAlert.ALERT_TOPIC = env.get('ALERT_TOPIC')
        KafkaAlert.NUM_PARTITIION = env.get('NUM_PARTITIION')
        KafkaAlert.REPLICATION_FACTOR = env.get('REPLICATION_FACTOR')

    def send_alert(self, service, users, duty_officers):
        KafkaAlert.send_kafka(self,service)
    def send_kafka(self, messageDto):
        message = json.dumps(messageDto.__dict__).encode()

        # Call produce function to send message to topic
        KafkaService.produceMessage(KafkaService,KafkaAlert.BOOTSTRAP_SERVER,KafkaAlert.ALERT_TOPIC,message)
        print('Sent to kafka successfuly')