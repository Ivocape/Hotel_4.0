from LogAndReg import * 

class App:
   






































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
        