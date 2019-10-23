from paciente import Paciente
from turno import Turno
from repositorio import Repositorio

class Gestion:
    
    def __init__(self):
        self.r = Repositorio()
        self.pacientes = self.r.get_all()
        #self.pacientes = []
        self.turnos = []

    def nuevo_paciente(self, apellido, nombre, dni, telefono, mail):
        paciente = Paciente(apellido, nombre, dni, telefono, mail)
        self.r.guardar(paciente)
        #self.pacientes.append(paciente)
        return paciente
        
    def _buscar_por_id(self,id_paciente):
        for paciente in self.pacientes:
            if str(paciente.id) == str(id_paciente):
                return paciente
        return None
    
    def modificar_paciente(self, id_paciente, apellido, nombre, dni, telefono, mail):        
        paciente = self._buscar_por_id(id_paciente)             
        if paciente:
            paciente.apellido = apellido
            paciente.nombre = nombre
            paciente.dni = dni
            paciente.telefono = telefono
            paciente.mail = mail
            self.r.actualizar(paciente) # !!
            return True
        return False            
               
    def eliminar_paciente(self, id_paciente):        
        paciente = self._buscar_por_id(id_paciente)
        if paciente:
            self.r.eliminar(paciente)
            #self.pacientes.remove(paciente)
            return True
        return False
    
    def _buscar_turno_id(self,id_turno):
        for turno in self.turnos:
            if str(turno.id_t) == str(id_turno):
                return paciente
        return None

    def asignar_turno(self, id_paciente, fecha_turno, hora, descripcion):
        paciente = self._buscar_por_id(id_paciente)
        turno = self.asignar_turno(paciente, fecha_turno, hora, descripcion)
        self.turnos.append(turno)
        
    def eliminar_turno(self, id_paciente):
        if turno:
            self.turnos.remove(turno)
            return True
        return False

    def modificar_turno(self, id_paciente, fecha_turno,hora, descripcion):        
        paciente = self._buscar_por_id(id_paciente)             
        if turno:
            turno.fecha_turno = fecha_turno
            turno.hora = hora
            turno.descripcion = descripcion
            return True
        return False
        
