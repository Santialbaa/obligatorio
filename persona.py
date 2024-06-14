from abc import ABC, abstractmethod

class Persona(ABC):    
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__fecha_nacimiento = fecha_nacimiento
        self.__fecha_ingreso = fecha_ingreso
        self.__celular = celular

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,value):
        self.__nombre = value

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self,value):
        self.__apellido = value

    @property
    def cedula(self):
        return self.__cedula
    
    @cedula.setter
    def cedula(self,value):
        self.__cedula = value

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self,value):
        self.__fecha_nacimiento = value

    @property
    def fecha_ingreso(self):
        return self.__fecha_ingreso
    
    @fecha_ingreso.setter
    def fecha_ingreso(self,value):
        self.__fecha_ingreso = value

    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self,value):
        self.__celular = value