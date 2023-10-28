# Defines an Array that Contains Every Instantiated User Class added
totalUsers = []

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
    def getInfo(self):
        print(self.typeUser)
        print(self.name)
        print(self.surname)
        print(self.email)
        print(self.password)

    # Returns the Name of a User
    def getName(self):
        return self.name

    # Returns the Surname of a User
    def getSurname(self):
        return self.surname

    # Returns the Email of a User
    def getEmail(self):
        return self.email

    # Returns the Password of a Certain User
    def getPassword(self):
        return self.password




# Returns a new instantiation of the User Class based off of user inputs
# Will return the User if the entries are valid, but will return False if they are not
""" def inputUser(nameEntry, surnameEntry, emailEntry, passwordEntry):
    name = str(input(nameEntry + " : "))
    surname = str(input(surnameEntry + " : "))
    email = str(input(emailEntry + " : "))
    password = str(input(passwordEntry + " : "))
    if validateInputs(name, surname, email, password):
        return createUser(name, surname, email, password)
    else:
        return False
 """
