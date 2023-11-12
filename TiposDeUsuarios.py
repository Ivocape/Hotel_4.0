

class User:

  
    def __init__(self,name="", surname="", email="", password="",typeUser=""):
        self.typeUser = typeUser
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
       
    def __str__(self) -> str:
        return (str(self.name) + " " + str(self.surname) + " " + str(self.email) + " " + str(self.password + " " + str(self.typeUser)) )



class Personal(User):
    def __init__(self,name, surname, email, password, typeUser,cargo,tarea):
        super().__init__(name, surname, email, password, typeUser)
        self.cargo=cargo
        self.tarea=tarea
    def __str__(self) -> str:
        return (str(self.name) + " " + str(self.surname) + " " + str(self.email) + " " + str(self.password + " " + str(self.typeUser)) )
    
class Cliente(User):
    def __init__(self, name, surname, email, password, typeUser):
        super().__init__(name, surname, email, password, typeUser)
        self.head=None
        
    def apilar(self,valor): #apila los gastos de un cliente
        from reservas import Nodo_recaudacion
        gasto=Nodo_recaudacion(valor)
        if self.head==None:
            self.head=gasto
        else:
            gasto.prox=self.head
            self.head=gasto
    
    def calcular_total(self): #calcula el total de gastos de un cliente
        aux=self.head
        totalgastos=0
        while aux!=None:
            totalgastos=totalgastos+aux.value
            aux=aux.prox
        return totalgastos
    def __str__(self) -> str:
        return (str(self.name) + " " + str(self.surname) + " " + str(self.email) + " " + str(self.password + " " + str(self.typeUser)) )
        

class Administrador(User):
    def __init__(self, name, surname, email, password, typeUser):
        super().__init__(name, surname, email, password, typeUser)
    def __str__(self) -> str:
        return (str(self.name) + " " + str(self.surname) + " " + str(self.email) + " " + str(self.password + " " + str(self.typeUser)) )
    