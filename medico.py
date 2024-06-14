from entities.persona import Persona

class Medico(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, especialidad):
        super().__init__(nombre,apellido,cedula,fecha_nacimiento,fecha_ingreso,celular)
        self.__especialidad = especialidad

    @property
    def especialidad(self):
        return self.__especialidad 
    
    @especialidad.setter
    def especialidad(self,value):
        self.__especialidad = value