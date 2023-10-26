from LogAndReg import * 
from managers import *
#class App:
   
#

start = input("¿Desea iniciar sesión? (s/n): ")
while start == "s":
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Modificar datos")
    print("4. Salir")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        inputtypeuser = input("Ingrese el tipo de usuario: ")
        inputnombre = input("Ingrese su nombre: ")
        inputapellido = input("Ingrese su apellido: ")
        inputemail = input("Ingrese su email: ")
        inputpassword = input("Ingrese su contraseña: ")
        if inputtypeuser == "admin":
            adminManager.createUser(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword)
       

    elif opcion == "2":
        inputemail = input("Ingrese su email: ")
        inputpassword = input("Ingrese su contraseña: ")
        
        userManager.validateUser(inputemail,inputpassword)
        if True:
            

            



    elif opcion == "3":
        pass
    elif opcion == "4":
        start = "n"
        
    else:
        print("Opción inválida")































import datetime

class Hotel:
    def __init__(self):
        
        self.clienteManager=Cliente_Manager()
        
    def menu(self):
        pass
    
class Persona:
    def __init__(self,nombre:str,apellido,dni:int,nacimiento):
        self.nombre: str =nombre
        self.apellido=apellido
        self.dni:int =dni
        self.nacimiento=nacimiento

        
        
        
class Cliente(Persona):
    
    def __init__(self, nombre, apellido, dni, nacimiento):
        super().__init__(nombre, apellido, dni, nacimiento)
    
class Cliente_Manager:
    def __init__(self):
        self.lista_clientes=set()
        
    def agregar_cliente(self,cliente):
        self.lista_clientes.add(cliente)
        


class Personal(Persona):
    def __init__(self, nombre, apellido, dni, nacimiento,cargo):
        super().__init__(nombre, apellido, dni, nacimiento)
        self.cargo=cargo
    
        
        
    

class Personal_Manager():
        def __init__(self):
            self.lista_empleado=set()
        def agregar_(self,personal):
            self.lista_empleado.add(personal)
        

class Admin(Personal):
    pass
class Mantenimiento:
    pass
        
class Limpieza:
    pass

class Habitacion:
    pass

class Reserva:
    pass

class Buffet:
    pass

if __name__ == "__main__":
    pass
        