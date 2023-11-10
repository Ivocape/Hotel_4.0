
# User Class that Provides the Structure for a User Object
# This class is what is created on invoking the createUser() function
class User:

    # User Class Constructor, Defines Variable Names in a Global Reach within the Class Object
    # Also appends the Object to the __totalUsers array on it's creation
    def __init__(self,name="", surname="", email="", password="",typeUser=""):
        self.typeUser = typeUser
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
       
    def __str__(self) -> str:
        return (str(self.name) + " " + str(self.surname) + " " + str(self.email) + " " + str(self.password + " " + str(self.typeUser)) )
    # Returns all info about a given user object


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
        
    def apilar(self,valor):
        from reservas import Nodo_recaudacion
        gasto=Nodo_recaudacion(valor)
        if self.head==None:
            self.head=gasto
        else:
            gasto.prox=self.head
            self.head=gasto
    
    def calcular_total(self):
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
    