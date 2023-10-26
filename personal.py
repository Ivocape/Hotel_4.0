class Personal(Persona):
    def __init__(self, nombre, apellido, dni, nacimiento,cargo):
        super().__init__(nombre, apellido, dni, nacimiento)
        self.cargo=cargo
        self.tarea=''
        self.ingresos_y_egresos={}
    def ingreso(self,fechaingreso,fechaegreso):
        self.ingresos_y_egresos
        #FALTA
        
class Tarea():
    def __init__(self,tarea,cargo):
        self.tarea=tarea
        self.cargo=cargo