from LogAndReg import User
class userManager:
    def __init__(self) -> None:
        self.totalUsers = []
        

    # Defines an Array that Contains Every Instantiated User Class added
   
    
    # Returns a new instantiation of the User Class for storage in a variable
    # Instantiations can be accessed later by accessing the __totalUsers array
    def createUser(self,name, surname, email, password):
        user = User(name, surname, email, password)
        self.totalUsers.append(user)
        return user

    # Returns a new instantiation of the User Class based off of user inputs
    # Will return the User if the entries are valid, but will return False if they are not
    def inputUser(self, nameEntry, surnameEntry, emailEntry, passwordEntry):
        name = str(input(nameEntry + " : "))
        surname = str(input(surnameEntry + " : "))
        email = str(input(emailEntry + " : "))
        password = str(input(passwordEntry + " : "))
        if validateInputs(name, surname, email, password): #tengo que ver como hacer esta funcion validadora
            return self.createUser(name, surname, email, password)
        else:
            return False



    # Validates the password of a specific user against a preset password
    # This will return  if the password is valid and False if it is not
    def validateUser(self, user, password):
    
        if user.password == password:
            return True
        else:
            return False

    #Lists all Users inside the totalUsers array without displaying passwords
    def listUsers(self):
        safeUsers = []
        for user in self.totalUsers:
            safeUsers.append({user.name, user.surname, user.email})
        return safeUsers

    # Lists all Users in the totalUsers array while displaying passwords
    def unsafeList():
        print("This function should only be used by Admins!")
        print("Make sure there are no other onlookers to this screen or it's output")
        print("Confirmation is required before displaying this information")
        conf = str(input("Are you sure you would like to display this information? (y/n)"))
        if conf == "y":
            for user in totalUsers:
                print(user.name)
                print(user.surname)
                print(user.email)
                print(user.password)
                return True
        else:
            return False

    # Checks all the Users to see if a password and email match is found
    # This will return True if a match is found, and False if not
    def userExists(email, password):
        for user in totalUsers:
            if user.email == email and user.password == password:
                return True
            else:
                return False

    # Removes a user based on their email as a primary key
    # Uses a list comprehension to reassign the totalUsers array with a filter for the email
    def removeUser(email):
        count = 0
        indexStore = []
        while count < len(totalUsers):
            if(totalUsers[count].email == email):
                indexStore.append(count)
            count += 1
        for index in indexStore:
            del(totalUsers[index])
        return True



