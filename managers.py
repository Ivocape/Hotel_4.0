from LogAndReg import User
class userManager:
    def __init__(self) -> None:
        self.totalUsers = []
        
        pass

     # Defines an Array that Contains Every Instantiated User Class added
   
    
    # Returns a new instantiation of the User Class for storage in a variable
    # Instantiations can be accessed later by accessing the __totalUsers array
    def createUser(self, typeUser ,name, surname, email, password):
        user = User(typeUser,name, surname, email, password)
        self.totalUsers.append(user)
        return user

    # Validates the password of a specific user against a preset password
    # This will return  if the password is valid and False if it is not
    def validateUser(self, user, password):
    
        if user.password == password:
            print ("Bienvenido, usted ha ingresado correctamente al sistema")
            return True
        else:
            print("La contraseña es incorrecta")
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


class Personal_Manager():
        def __init__(self):
            self.lista_empleado=set()
            self.lista_tareas=[]         
        def agregar_personal(self,personal):
            self.lista_empleado.add(personal)
        def dar_de_baja(self,personal):
            self.lista_empleado.remove(personal)
        def nuevatarea(self,tarea):
            self.lista_tareas.append(tarea)
        def asignacion_tareas(self,user): #Asignarle una tarea a un determinado empleado
            if user.tarea == None:
                for i in range(len(self.lista_tareas)):
                    if user.cargo==self.lista_tareas[i].cargo:
                        self.tarea=self.lista_tareas.pop(i)
                        break
            else:
                print('Empleado no disponible')
        def asignacion_tareas_todos(self): #Asignarle tareas a todos
            for i in range(len(self.lista_empleado)):
                if self.lista_empleado[i].tarea == None:
                    for j in range(len(self.lista_tareas)):
                        if self.lista_empleado[j].cargo==self.lista_tareas[j].cargo:
                            self.tarea=self.lista_tareas.pop(j)
                            break
                        else:
                            print('No hay tareas disponibles para el cargo')
                else:
                    print('Empleado {} no disponible'.format(self.lista_empleado[i].nombre))


class Habitacion_Manager():
    def __init__ (self):
          self.lista_habitaciones=[]
    def agregar_(self,habitacion):
        self.lista_habitaciones.append(habitacion)
    def ocupar_habitacion (self,nro_habitacion):
            for i in range(len(self.lista_habitaciones)):
                if self.lista_habitaciones[i].nro_habitacion==nro_habitacion:
                    if self.lista_habitaciones[i].ocupacion == True:
                        print('La habitacion esta ocupada')
                    else: 
                        self.lista_habitaciones[i].ocupacion = True
                        
                        
class Reserva_Manager():
    def __init__ (self):
        self.reservas={ }
    def agregar_reserva (self, reserva):
        self.reservas[reserva.nro_reserva]= reserva