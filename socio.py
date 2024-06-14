from entities.persona import Persona

class Socio(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, tipo):
        super().__init__(nombre,apellido,cedula,fecha_nacimiento,fecha_ingreso,celular)
        self.__tipo = tipo
        self.__deuda = 0

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self,value):
        self.__tipo = value

    @property
    def deuda(self):
        return self.__deuda
    
    @deuda.setter
    def deuda(self,value):
        self.__deuda = value

    