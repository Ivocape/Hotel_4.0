from LogAndReg import User
class Personal(User):
    def __init__(self, name, surname, email, password, cargo, sueldo):
        super().__init__(name, surname, email, password)
        
        self.cargo = cargo
        self.sueldo = sueldo

class Cliente(User):
    def __init__(self, name, surname, email, password, dni, fecha_nacimiento):
        super().__init__(name, surname, email, password)
        
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento

class Administrador(User):
    def __init__(self, name, surname, email, password):
        super().__init__(name, surname, email, password)
        
    ############################# Creo que esto no va aca, y va en personalManager #############################
    
    # def __init__(self, nombre, apellido, dni, nacimiento,cargo):
    #     super().__init__(nombre, apellido, dni, nacimiento)
    #     self.cargo=cargo
    #     self.tarea=''
    #     self.ingresos_y_egresos={}
    # def ingreso(self,fechaingreso,fechaegreso):
    #     self.ingresos_y_egresos
    #     #FALTA
        
    # class Tarea():
    #     def __init__(self,tarea,cargo):
    #         self.tarea=tarea
    #         self.cargo=cargo