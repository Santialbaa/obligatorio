class Especialidad:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,value):
        self.__nombre = value

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,value):
        self.__precio = value