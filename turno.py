import datetime
ultima_id_t = 0 # agregamos global id
from paciente import Paciente
class Turno:
    def __init__(self, paciente, fecha_turno, hora, descripcion, id_turno = None):
        self.paciente = paciente
        self.fecha_turno = fecha_turno
        self.descripcion = descripcion
        self.hora = hora
        self.hora_real = None
        ##  Revisar:
        fecha_creacion = datetime.datetime.today()

    # agregamos global id    
        global ultima_id_t
        ultima_id_t += 1
        self.id_t = id_turno

