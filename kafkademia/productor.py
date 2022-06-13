from .ejemplos import ATM, Sensor
import json
from kafka import KafkaProducer
import random
from time import sleep

class Productor(object):
    def __init__(self, bootstrap_servers:str, topico:str):
        self.bootstrap_servers = bootstrap_servers
        self.topico = topico
        # Esto permite instanciar el productor de Kafka con la lista de
        # bootstrap_servers. Mas parámetros se pueden encontrar en:
        #  https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html#
        self.productor = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            # Los mensajes se serializan en formato JSON
            value_serializer=lambda m: json.dumps(m).encode("utf-8"),
        )

    def producir(self, ejemplo:str="sensor", cant_mensajes: int = 100, delay=True):        
        caso = ejemplo.lower()
        if caso == "sensor":
            ej = Sensor()
        elif caso == "atm":
            ej = ATM()
        
        for _ in range(cant_mensajes):
            if delay:
                sleep(random.randint(1, 3))
            ej.generar_mensaje()