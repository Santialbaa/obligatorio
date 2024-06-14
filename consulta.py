class Consulta:
    def __init__(self, especialidad, medico, fecha, max_pacientes):
        self.__especialidad = especialidad
        self.__medico = medico
        self.__fecha = fecha
        self.__max_pacientes = max_pacientes
        self.__pacientes = [""] * max_pacientes

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self,value):
        self.__especialidad = value

    @property
    def medico(self):
        return self.__medico
    
    @medico.setter
    def medico(self,value):
        self.__medico = value

    @property
    def fecha(self):
        return self.__fecha 
    
    @fecha.setter
    def fecha(self,value):
        self.__fecha = value

    @property
    def max_pacientes(self):
        return self.__max_pacientes
    
    @max_pacientes.setter
    def max_pacientes(self,value):
        self.__max_pacientes = value
    
    @property
    def pacientes(self):
        return self.__pacientes
    
    @pacientes.setter
    def pacientes(self,value):
        self.__pacientes = value

    