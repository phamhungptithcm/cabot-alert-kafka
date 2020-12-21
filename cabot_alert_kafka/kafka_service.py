from kafka import KafkaAdminClient, KafkaProducer
from kafka.admin import NewTopic
from kafka.errors import KafkaError


class KafkaService():
    def produceMessage(self, bootstrapServer, topic, jsonMessage):
        try:
            producer = KafkaProducer(bootstrap_servers=bootstrapServer)
            print('Sending message to topic %s ' % topic)
            producer.send(topic, jsonMessage)
            print('Sent successfully')
            producer.close()
        except KafkaError as e:
            print('Error to send kafka %s' % e)
            pass

    def createTopic(self,bootstrapServer,topic, numPartitions, replicationFactor):
        try:
            admin = KafkaAdminClient(bootstrapServer)
            topic = NewTopic(name=topic,
                             num_partitions=numPartitions,
                             replication_factor=replicationFactor)
            admin.create_topics([topic])
        except Exception as e:
            print('Error to create topic %s' % e)
            pass



