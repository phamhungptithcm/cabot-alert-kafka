from models import KafkaAlert

class MessageDto:
    serviceStatus=''
    serviceName=''
    def __init__(self, serviceStatus, serviceName):
        self.serviceStatus = serviceStatus
        self.serviceName = serviceName
messageDto = MessageDto('PASSING_STATUS', '')
KafkaAlert.send_kafka(KafkaAlert,messageDto)



