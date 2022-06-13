from datetime import datetime
import random
from uuid import uuid4

class ATM(object):
    def __init__(self, mov_min:int=-5000, mov_max:int=5000):
        self.user_id = str(uuid4())
        self.mov_min = mov_min
        self.mov_max = mov_max
    
    def generar_mensaje(self):
        movimiento = random.randint(self.mov_min, self.mov_max)
        hora = datetime.now().strftime("%H:%M:%S")

        mensaje_atm = {
            "id_usuario" : self.user_id,
            "hora" : hora,
            "movimiento" : movimiento
        }
        return mensaje_atm

class Sensor(object):
    def __init__(self, id_sen_min:int=1, id_sen_max:int=9, temp_min:int=15, temp_max:int=18):
        self.id_sen_min = id_sen_min
        self.id_sen_max = id_sen_max
        self.temp_min = temp_min
        self.temp_max = temp_max
        pass

    def generar_mensaje(self):
        id = random.randint(self.sen_min, self.sen_max)
        temp = random.randint(self.temp_min, self.temp_max)
        hora = datetime.now().strftime("%H:%M:%S")
        mensaje_sensor = {
            "id": id,
            "hora": hora,
            "temperatura": temp
        }
        return mensaje_sensor