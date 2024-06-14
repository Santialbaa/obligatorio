from datetime import datetime
from entities.socio import Socio
from entities.medico import Medico
from entities.especialidad import Especialidad 
from entities.consulta import Consulta

# ".isdigit" significa que tienen que ser digitos, si no da error
# ".isalpha" significa que tienen que ser letras, si no da error
# ".startswith" significa que tiene que empezar con el argumento dado
# "ValueError" significa que no se ha ingresado como int
# "if not" en caso de que no se cumpla la condicion proporcionada

class Policlinica():
    
    def __init__(self):

        # Creo todas las matrices
        self.especialidades = []
        self.socios = []
        self.medicos = []
        self.consultas = []

    def dar_alta_especialidad(self):

        while True:
            while True:
                nombre = input("Ingrese el nombre de la especialidad: ")
                # Escribo el input del nombre junto con su error 
                if not nombre.isalpha():
                    print("El nombre de la especialidad es incorrecto, ingreselo nuevamente")
                    continue
                break
            while True:          
                # Escribo el exception de que el precio sea un numero
                precio = input("Ingrese el precio asociado: ")
                if not precio.isdigit():
                    print("El precio de la especialidad es incorrecto, igreselo nuevamente")
                    continue
                break
            # Appendeo la especialida a la matriz
            e = Especialidad(nombre,precio)
            self.especialidades.append(e)
            print(self.especialidades)
            print("La especialidad se ha creado con exito")
            break

    def dar_alta_socio(self):

        while True:
            while True:
                # Escribo el input del nombre junto con su error
                nombre = input("Ingrese el nombre: ")
                if not nombre.isalpha():
                    print("No es un nombre valido, ingreselo de nuevo")
                    continue
                break
            while True:
                # Escribo el input del apellido junto con su error
                apellido = input("Ingrese el apellido: ")
                if not apellido.isalpha():
                    print("No es un apellido valido, ingreselo de nuevo")
                    continue
                break
            while True:
                # Escribo el input de la cedula junto con su error
                cedula = input("Ingrese la cedula: ")
                if not (cedula.isdigit() and len(cedula) == 8):
                    print("No es una cedula valida, ingrese nuevamente una cedula de 8 digitos")
                    continue
                for cedula_s in self.socios:
                    if cedula_s.cedula == cedula:
                            print("Ya existe un socio registrado con esa cedula")
                            return False
                break
            while True:
                # Escribo el input de la fecha de nacimiento junto con su error
                fecha_nacimiento = input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
                if not self.es_fecha_valida(fecha_nacimiento):
                    print("No es una fecha valida, vuelva a ingresarla en el formato aaaa-mm-dd")
                    continue
                break
            while True:
                # Escribo el input de la fecha de ingreso junto con su error
                fecha_ingreso = input("Ingrese la fecha de ingreso a la institucion en el formato aaaa-mm-dd: ")
                if not self.es_fecha_valida(fecha_ingreso):
                    print("No es una fecha valida, vuelva a ingreserla en el formato aaaa-mm-dd")
                    continue
                break
            while True:
                # Escribo el numero de celular junto con su error
                celular = input("Ingrese el numero de celular: ")
                if not (celular.isdigit() and len(celular) == 9 and celular.startswith("09")):
                    print("No es un numero de celular valido, ingrese un numero con el formato 09XXXXXXX")
                    continue
                break
            while True:
                # Escribo el tipo de bonificacion junto con su error
                tipo = input("Ingrese el tipo de socio: 1- Bonificado 2- No Bonificado: ")
                if tipo not in ["1", "2"]:
                    print("El valor ingresado no correcto, elige la opcion 1 o 2")
                    continue
                break

            # Appendeo el socio a la matriz
            s = Socio(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular, tipo)
            self.socios.append(s)
            print(self.socios)
            print("El socio se ha creado con exito")
            break

    def dar_alta_medico(self):

        especialidad_string = False
        especialidad_existe = False
        especialidad_medico = None
        
        while True:
            while True:
                # Escribo el nombre junto a su error
                nombre = input("Ingrese el nombre: ")
                if not nombre.isalpha():
                    print("No es un nombre valido, ingreselo de nuevo")
                    continue
                break
            while True:
                # Escribo el apellido junto a su error
                apellido = input("Ingrese el apellido: ")
                if not apellido.isalpha():
                    print("No es un apellido valido, ingreselo de nuevo")
                    continue
                break
            while True:
                # Escribo la cedula junto a su error
                cedula = input("Ingrese la cedula de indentidad: ")
                if not (cedula.isdigit() and len(cedula) == 8):
                    print("No es una cedula valida, ingrese nuevamente una cedula de 8 digitos")
                    continue
                break
            while True:
                # Escribo la fecha de nacimiento junto a su error
                fecha_nacimiento = input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
                if not self.es_fecha_valida(fecha_nacimiento):
                    print("No es una fecha valida, vuelva a ingresarla en el formato aaaa-mm-dd")
                    continue
                break
            while True:
                # Escribo la fecha de ingreso junto a su error
                fecha_ingreso = input("Ingrese la fecha de ingreso a la institucion en el formato aaaa-mm-dd: ")
                if not self.es_fecha_valida(fecha_ingreso):
                    print("No es una fecha valida, vuelva a ingresarla en el formato aaaa-mm-dd")
                    continue
                break
            while True:
                # Escribo el numero de celular junto a su error
                celular = input("Ingrese numero celular: ")
                if not (celular.isdigit and len(celular) == 9 and celular.startswith("09")):
                    print("No es un numero de celular valido, ingrese un numero con el formato 09XXXXXXX")
                    continue
                break
            
            while True:
                # Escribo la especialidad junto a su error
                while True:
                    especialidad = input("Ingrese la especialidad: ")
                    if not especialidad.isalpha():
                        print("Esta especialidad debe de ser un string")   
    
                # Si no se encuentra la especialidad
                    if self.buscar_especialidad(especialidad) == None:
                        print("Esta especialidad no esta dada de alta")
                        # Creo un loop para decidir que hacer con la nueva especialidad
                        # si descartarla o agregarla
                        while True:
                            print("1 - Volver a ingresar la especialidad")
                            print("2 - Dar de alta esta especialidad")
                            opcion = input("Elija una opcion: ")
                            if opcion == "1":
                                break
                            elif opcion == "2":
                                self.dar_alta_especialidad()
                                especialidad = self.buscar_especialidad(especialidad)
                                break
                            else:
                                print("Opcion incorrecta, eliga nuevamente")
                                continue
                    else:
                        break
                    
                break
            m = Medico(nombre,apellido,cedula,fecha_nacimiento,fecha_ingreso,celular,especialidad)
            self.medicos.append(m)
            print("El medico se ha creado con exito")
            print (self.medicos)
            break
        
        
    
    def dar_alta_consulta(self):

        while True:

            especialidad = input("Ingrese la especialidad: ")
            if not especialidad.isalpha():
                print("La especialidad debe ser un string")
                continue

            while True: 
                especialidad_consulta = self.buscar_especialidad(especialidad)
                if especialidad_consulta is None:
                    print("Esta especialidad no esta dada de alta")
                    while True:
                        print("1 - Volver a ingresar la especialidad")
                        print("2 - Dar de alta esta especialidad")
                        opcion = input("Elija una opcion: ")
                        if opcion == "1":
                            break
                        elif opcion == "2":
                            self.dar_alta_especialidad()
                            especialidad_consulta = self.buscar_especialidad(especialidad)
                            break
                        else:
                            print("Opcion incorrecta, eliga nuevamente")
                            continue
                break

            nombre_medico = input("Ingrese el nombre del medico: ")
            medico_consulta = self.buscar_medico(nombre_medico,especialidad_consulta)
            if medico_consulta is None:
                print("Este medico no esta dado de alta")
                while True:
                    print("1 - Volver a ingresar el medico")
                    print("2 - Dar de alta el medico")
                    opcion = input("Elija una opcion: ")
                    if opcion == "1":
                        break
                    elif opcion == "2":
                        self.dar_alta_medico()
                        medico_consulta = self.buscar_medico(nombre_medico,especialidad_consulta)
                        break
                    else:
                        print("Opcion incorrecta, elija nuevamente")
                if medico_consulta is None:
                    continue

            fecha_consulta = input("Ingrese la fecha de consulta en formato aaaa-mm-dd: ")
            if not self.es_fecha_valida(fecha_consulta):
                print("No es una fecha valida, vuelva a ingresarla en el formato aaaa-mm-dd")
                continue

            try:
                max_pacientes = int(input("Ingrese la cantidad de pacientes que se atenderan: "))
            except ValueError:
                print("La cantidad de pacientes debe ser un numero entero")
                continue

            self.consultas.append(Consulta(especialidad_consulta,medico_consulta,fecha_consulta,max_pacientes))
            print("La consulta se ha creado con exito")
            break
 
    def emitir_ticket(self):
        while True:

            listado = 0
            
            while True:
                especialidad = input("Ingrese especialidad: ")
                if not especialidad.isalpha():
                    print("El nombre de la especialidad es incorrecto, ingreselo nuevamente")
                break
            
            lista_consultas = []
            for med_con in self.consultas:
                if especialidad == med_con.especialidad:
                    listado += 1
                    lista_consultas.append(listado,med_con)
                    print(f"{listado}. Medico: {med_con.medico} de la consulta: {med_con.fecha}")

            seleccion = str(input("Eliga una opcion: "))

            for consulta in lista_consultas:
                if seleccion == consulta[0]:
                    cupos = [numero for numero, cupo in enumerate(consulta.max_pacientes, 1) if cupo == 0]
                    print (f"los cupos disponibles son {cupos}")
            
            cupo_selec = input("Elija una opcion:")


            while True: #Reescribir estp como lo de especialiadd, copia y pega
                ci = (input("Ingrese la cedula del socio: "))
                if not (ci.isdigit and len(ci) == 8):
                        print("No es una cedula valida, ingrese nuevamente una cedula de 8 digitos")
                        continue
                for cedula_s in self.socios:
                    if cedula_s.cedula != ci:
                        print("No existe un socio registrado con esa cedula")
                        return False
                break
            
            cedula_ticket = self.buscar_cedula(ci)
            if cedula_ticket is None:
                print("Este socio no esta dado de alta")
                while True:
                    print("1 - Volver a ingresar la cedula")
                    print("2 - Dar de alta el socio")
                    opcion = input("Elija una opcion: ")
                    if opcion == "1":
                        break
                    elif opcion == "2":
                        self.dar_alta_socio()
                        medico_consulta = self.buscar_cedula(ci)
                        break
                    else:
                        print("Opcion incorrecta, elija nuevamente")
                if medico_consulta is None:
                    continue
            
            for socio in self.socios:
                if cedula_ticket == socio.cedula:
                    if socio.tipo == 1:
                        socio.deuda += 0.8 * especialidad.precio
                    elif socio.tipo == 2:
                        socio.deuda += especialidad.precio

            #Falta hacer que se cambie la posicion cupo_selec-1 de consulta.max_pacientes por ci de ticket

            

    def realizar_consultas(self):
        while True:
            print("Seleccione una opcion:")
            print("1. Obtener todos los medicos asociados a una especialidad especifica")
            print("2. Obtener el precio de una consulta de una especialidad en especifico")
            print("3. Listar todos los socios con sus deudas asociadas en orden ascendente")
            print("4. Realizar consultas respecto a cantidad de consultas entre dos fechas")
            print("5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas")
            print("6. Volver")
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                especialidad = input("Ingrese especialidad: ")
                especialidad_m = self.buscar_especialidad(especialidad)
                if especialidad_m is None:
                    print("Esa especialidad no esta dada de alta")
                else:
                    print(f"{especialidad.nombre}")
                    for medico in self.medicos:
                        if medico.especialidad == especialidad_m:
                            print(f"Medico: {medico.nombre} {medico.apellido}")
                    else:
                        print("No hay medicos asociados a esta especialidad")
                    break
            elif opcion == "2":
                especialidad = input("Ingrese especialidad: ")
                for especialidad in self.especialidades:
                    print(f"{especialidad.nombre} - ${especialidad.precio}")
                return""
            elif opcion == "3":
               
                self.socios.sort(key=lambda x: x.deuda)
                for socio in self.socios:
                    print(f"{socio.apellido}, {socio.nombre} - ${socio.deuda}")
                return ""

            elif opcion == "4":
                while True:
                    # Escribo la fecha final junto a su error
                    
                    fecha_inicial = input("Ingrese la fecha inicial en formato aaaa-mm-dd:")
                    if not self.es_fecha_valida(fecha_inicial):
                        print("ingrese la fecha inicial en formato aaaa-mm-dd: ")
                        continue
                    break
                while True:
                    # Escribo la fecha final junto a su error
                    fecha_final = input("Ingrese la fecha final en formato aaaa-mm-dd:")
                    if not self.es_fecha_valida(fecha_final):
                        print("ingrese la fecha final en formato aaaa-mm-dd: ")
                        continue
                    break
                cantidad_cons = 0 
                for consulta in self.consultas:
                    if  fecha_inicial <= consulta.fecha <= fecha_final:
                        cantidad_cons+=1
                print(cantidad_cons)

                continue

                
            elif opcion == "5":
                while True:
                    # Escribo la fecha final junto a su error
                    fecha_inicial = input("Ingrese la fecha inicial en formato aaaa-mm-dd:")
                    if not self.es_fecha_valida(fecha_inicial):
                        print("no es una fecha valida, vuelva a ingresarla en formato aaaa-mm-dd: ")
                        continue
                    break
                while True:
                    # Escribo la fecha final junto a su error
                    fecha_final = input("Ingrese la fecha final en formato aaaa-mm-dd:")
                    if not self.es_fecha_valida(fecha_final):
                        print("no es una fecha valida, vuelva a ingresarla en formato aaaa-mm-dd: ")
                        continue
                    break
                ganancias = 0
                for consulta in self.consultas:
                    if  fecha_inicial <= consulta.fecha <= fecha_final:
                        ganancias += consulta.precio
                print(ganancias)
                continue
            
            elif opcion == "6":
                print("Volviendo")
                break
    
    # Funcion para que verifique si la fecha se encuentra con el formato correcto
    def es_fecha_valida(self, fecha):
        try:
            # Convierto un string a formato de fecha con strptime con los
            # argumentos, primero indica la fecha que se ingresa y luego 
            # el formato al que pasara a estar esa fecha
            datetime.strptime(fecha, "%Y-%m-%d")
            return True
        except ValueError:
            return False
        
    # Funcion para buscar la especialidad en la matriz y decidir que hacer
    def buscar_especialidad(self,nombre):
        # Busca la especialidad en la matriz
        for especialidad in self.especialidades:
            # Si se encuentra una especialidad bajo ese nombre
            if especialidad.nombre == nombre:
                # Devuelve la especialidad
                return especialidad
        # Si no lo encuentra devuelve None
        return None
            
    # Funcion para buscar el medico en la matriz y decidir que hacer 
    def buscar_medico(self,nombre,especialidad):
        # Busca el medico en la matriz
        for medico in self.medicos:
            # Si encuentra al medico bajo ese nombre
            if medico.nombre == nombre and medico.especialidad == especialidad:
                # Devuelve el medico
                return medico
        # Si no lo encuentra devuelve None
        return None
    
    def buscar_cedula(self,ci):
        for cedula in self.socios:
            if ci == cedula.cedula:
                return ci

    def get_mats(self):
        while True:
            print("Seleccione una opcion:")    
            print("1. Mostrar matriz de socios")
            print("2. Mostrar matriz de medicos")
            print("3. Mostrar matriz de especialidades")
            print("4. Mostrar matriz de consultas")
            print("5. Volver")
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                for socio in self.socios:
                    print(f"{socio.cedula} - {socio.apellido}, {socio.nombre}")
            elif opcion == "2":
                for medico in self.medicos:
                    print(f"{medico.cedula} - {medico.apellido}, {medico.nombre} - {medico.especialidad.nombre}")
            elif opcion == "3":
                for especialidad in self.especialidades:
                    print(f"{especialidad.nombre} - ${especialidad.precio}")
            elif opcion == "4":
                for consulta in self.consultas:
                    print(f"{consulta.especialidad} - Medico: {consulta.medico} - {consulta.fecha} - {consulta.max_pacientes} - {consulta.pacientess}")
            elif opcion == "5":
                break
            else:
                print("La opcion seleccionada no es correcta, vuelva a intentar con otra opcion")

def main():

    policlinica = Policlinica()
    while True:
        print("Seleccione una opcion del menu:")
        print("1. Dar de alta una especialidad")
        print("2. Dar de alta un socio")
        print("3. Dar de alta un medico")
        print("4. Dar de alta una consulta medica")
        print("5. Emitir un ticket de consulta")
        print("6. Realizar consultas")
        print("7. Mostrar matrices")
        print("8. Salir del programa")

        opcion = input("Ingrese una opcion: ")
        if opcion == '1':
            policlinica.dar_alta_especialidad()
        elif opcion == '2':
            policlinica.dar_alta_socio()
        elif opcion == '3':
            policlinica.dar_alta_medico()
        elif opcion == '4':
            policlinica.dar_alta_consulta()
        elif opcion == '5':
            policlinica.emitir_ticket()
        elif opcion == '6':
            policlinica.realizar_consultas()
        elif opcion == '7':
            policlinica.get_mats()
        elif opcion == '8':
            print("Saliendo del programa...")
            break
        else:
            print("La opcion seleccionada no es correcta, vuelva a intentar con otra opcion")

if __name__ == "__main__":
    main()
