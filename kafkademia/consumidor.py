from kafka import KafkaConsumer

class Consumidor(object):
    def __init__(self, bootstrap_servers:str, topico:str):
        self.bootstrap_servers = bootstrap_servers
        self.topico = topico
        # Esto permite instanciar el consumidor de Kafka con la lista de
        # bootstrap_servers y el topico. Mas parámetros se pueden encontrar en:
        #  https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#
        self.consumidor = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            topic=topico
        )

    def consumir(self):
        for msg in self.consumidor:
            print(msg)