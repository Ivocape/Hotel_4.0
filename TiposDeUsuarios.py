
# User Class that Provides the Structure for a User Object
# This class is what is created on invoking the createUser() function
class User:

    # User Class Constructor, Defines Variable Names in a Global Reach within the Class Object
    # Also appends the Object to the __totalUsers array on it's creation
    def __init__(self,typeUser="",name="", surname="", email="", password=""):
        self.typeUser = typeUser
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
       
    def __str__(self) -> str:
        return (str(self.typeUser)+" "+ str(self.name) + " " + str(self.surname) + " " + str(self.email) + " " + str(self.password) )
    # Returns all info about a given user object


class Personal(User):
    def __init__(self,name, surname, email, password):
        super().__init__(name, surname, email, password)
    def __str__(self) -> str:
        return (str(self.typeUser)+" "+ str(self.name) + " " + str(self.surname) + " " + str(self.email) + " " + str(self.password) )
    
class Cliente(User):
    def __init__(self, name, surname, email, password):
        super().__init__(name, surname, email, password)
    def __str__(self) -> str:
        return (str(self.typeUser)+" "+ str(self.name) + " " + str(self.surname) + " " + str(self.email) + " " + str(self.password) )
        

class Administrador(User):
    def __init__(self, name, surname, email, password):
        super().__init__(name, surname, email, password)
    def __str__(self) -> str:
        return (str(self.typeUser)+" "+ str(self.name) + " " + str(self.surname) + " " + str(self.email) + " " + str(self.password) )
    