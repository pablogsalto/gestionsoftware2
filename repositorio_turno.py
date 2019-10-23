import sqlite3
from turno import Turno

class Repositorio_Turno:
    ###Consulta y guarda turnos en la BD###

    def __init__(self):
        self.bd = sqlite3.connect ("turnos.db")
        self.cursor = self.bd.cursor()

    def get_all(self):
        ###Retorna una lista de objetos Turno con todos los turnos que haya guardados en la BD###
        lista_turnos = []
        consulta = "SELECT id, descripcion, etiquetas, fecha_creacion, fecha_turno, hora_real, id_paciente, pagado, asistio, cancelo FROM turnos;"
        self.cursor.execute(consulta)
        todos_los_turnos = self.cursor.fetchall()
        for id, descripcion, etiquetas, fecha_creacion, fecha_turno, hora_real, id_paciente, pagado, asistio, cancelo in todos_los_turnos:
            if etiquetas:
                ###Crear turno sin etiquetas
                lista_turnos.append(Turno(id, descripcion, "Sin etiquetas", fecha_creacion, fecha_turno, hora_real, id_paciente, pagado, asistio, cancelo)) #probar y revisar cuando este el objeto turno

            else:
                lista_turnos.append(Turno(id, descripcion, etiquetas, fecha_creacion, fecha_turno, hora_real, id_paciente, pagado, asistio, cancelo))
        return lista_turnos

    def guardar (self, turnos):
        ###Guarda el turno en la BD### #probar y revisar!!! #ver que onda id_paciente
        consulta = "INSERT INTO turnos (descripcion, etiquetas, fecha_creacion, fecha_turno, hora_real, id_paciente, pagado, asistio, cancelo VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
        resultado = self.cursor.execute(consulta, [turnos.descripcion, turnos.etiquetas, turnos.fecha_creacion, turnos.fecha_turno, turnos.hora_real, turnos.id_paciente, turnos_pagado, turnos_asistio, turnos.cancelo])
        id_turnos = resultado.lastrowid #revisar!!!
        self.bd.commit()
        return id_turnos

    def actualizar (self, turnos):
        ###Actualiza el turno en la BD### #ver que onda turnos.id
        consulta = "UPDATE turnos SET etiquetas = ? WHERE id = ?;"
        self.cursor.execute(consulta, [turnos.etiquetas, turnos.id])
        self.bd.commit()

    def eliminar (self, turnos):
        ###Elimina el turno de la BD###
        consulta = "DELETE FROM turnos WHERE id = ?;"
        self.cursor.execute(consulta, [turnos.id])
        self.bd.commit()
        
