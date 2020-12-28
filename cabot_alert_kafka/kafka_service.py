from kafka import KafkaAdminClient, KafkaProducer
from kafka.admin import NewTopic
from kafka.errors import KafkaError

import logging

logger = logging.getLogger(__name__)


class KafkaService():
    def produceMessage(self, bootstrapServer, topic, jsonMessage):
        try:
            producer = KafkaProducer(bootstrap_servers=bootstrapServer)
            logger.info('Sending message to topic %s ' % topic)
            producer.send(topic, jsonMessage)
            logger.info('Sent successfully')
            producer.close()
        except KafkaError as e:
            logger.error('Error to send kafka %s' % e)
            pass

    def createTopic(self,bootstrapServer,topic, numPartitions, replicationFactor):
        try:
            admin = KafkaAdminClient(bootstrapServer)
            topic = NewTopic(name=topic,
                             num_partitions=numPartitions,
                             replication_factor=replicationFactor)
            admin.create_topics([topic])
        except Exception as e:
            logger.error('Error to create topic %s' % e)
            pass



