import datetime
#ultima_id = 0
class Paciente:
    def __init__(self,apellido,nombre,dni,telefono,mail,id_paciente = None):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.mail = mail
        self.fecha_creacion = datetime.datetime.today()
        #global ultima_id
        #ultima_id += 1
        #self.id = ultima_id
        self.id = id_paciente

    def coincide(self, filtro):
        return (filtro in self.apellido) or (filtro in self.dni)
