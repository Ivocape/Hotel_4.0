from TiposDeUsuarios import *
from discoDuro import *
from habitacion import *
import datetime
from reservas import *

class userManager:
    def __init__(self) -> None:
        self.totalUsers = [] ######### Aca Vamos a tener un problema #####
    
    # Returns a new instantiation of the User Class for storage in a variable
    # Instantiations can be accessed later by accessing the __totalUsers array
    def createUser(self, typeUser ,name, surname, email, password):
        user = User(typeUser,name, surname, email, password)
        self.totalUsers.append(user)
        return user

    # Validates the password of a specific user against a preset password
    # This will return  if the password is valid and False if it is not
    def validateUser(self,email, password):
        #aca tengo que hacer un for para leer una lista de usuarios y encontrar el usuario que quiero. luego comparar las contraseñas.
        for user in discoHotel1.users:
            if user['email'] == email:    
                if password == user['password']:
                    print ("Bienvenido, usted ha ingresado correctamente al sistema")
                    return True
                else:
                    print("La contraseña es incorrecta")
                    return False
            else:
                print("El usuario no existe")
                return False


    #Lists all Users inside the totalUsers array without displaying passwords
    def listUsers(self):
        safeUsers = []
        for user in self.totalUsers:
            safeUsers.append({user.name, user.surname, user.email})
        return safeUsers

    # Lists all Users in the totalUsers array while displaying passwords
    def unsafeList(self):
        print("This function should only be used by Admins!")
        print("Make sure there are no other onlookers to this screen or it's output")
        print("Confirmation is required before displaying this information")
        conf = str(input("Are you sure you would like to display this information? (y/n)"))
        if conf == "y":
            for user in self.totalUsers:
                print(user.name)
                print(user.surname)
                print(user.email)
                print(user.password)
                return True
        else:
            return False
    
    # Checks all the Users to see if a password and email match is found
    # This will return True if a match is found, and False if not
    def userExists(self,email, password):
        for user in self.totalUsers:
            if user.email == email and user.password == password:
                return True
            else:
                return False

    # Removes a user based on their email as a primary key
    # Uses a list comprehension to reassign the totalUsers array with a filter for the email
    def removeUser(self, email):
        count = 0
        indexStore = []
        while count < len(self.totalUsers):
            if(self.totalUsers[count].email == email):
                indexStore.append(count)
            count += 1
        for index in indexStore:
            del(self.totalUsers[index])
        return True


class adminManager:
    def __init__(self) -> None:
        self.totalAdmins = []
    
    def createAdmin(self,typeUser ,name, surname, email, password):
        admin = Administrador(name, surname, email, password)
        self.totalAdmins.append(admin)
        userManager.createUser(self ,typeUser, name, surname, email, password)

        return admin

class personalManager():
    def __init__(self):
        self.lista_empleado=[] #Yo tengo una lista de empleados(La instancia de personalManager)
        self.lista_tareas=[]      
        self.registros=[]
    def createPersonal(self,typeUser ,name, surname, email, password): 
     
        personal = Personal(name, surname, email, password)
        print(personal)
        #self.lista_empleado.add(personal)
        from Index import instance #Aca importamos la instancia de la clase Hotel
        instance.userManager.createUser(typeUser, name, surname, email, password)

    def agregar_personal(self,personal):
        self.lista_empleado.add(personal) ####### no entiendo como funciona esto #######

    def dar_de_baja(self,personal):
        self.lista_empleado.remove(personal) 
        #Aca necesitamos generar un metodo que elimine al personal de la lista de empleados en el CSV
    def nuevatarea(self,tarea):
        self.lista_tareas.append(tarea)
    def asignacion_tareas(self,user): #Asignarle una tarea a un determinado empleado y Guardarla en el CSV
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
                
    def registrar_ingreso(self,empleado):
        self.registros.append(['Ingreso',empleado,datetime.datetime.now()])
    def registrar_egreso(self,empleado):
        self.registros.append(['Egreso',empleado,datetime.datetime.now()])
    
    
class clienteManager():
    def __init__(self):
        self.lista_cliente=[]
        
    def agregar_cliente(self,cliente):
        self.lista_cliente.append(cliente)
    def dar_de_baja(self,cliente):
        self.lista_cliente.remove(cliente)
        #Aca necesitamos generar un metodo que elimine al cliente de la lista de clientes en el CSV
    def createCliente(self,typeUser ,name, surname, email, password):
        cliente = Cliente(name, surname, email, password)
        self.lista_cliente.append(cliente)
        DiscoDuro().escribir(name, surname, email, password)
        DiscoDuro().leer()
        from Index import instance #Aca importamos la instancia de la clase Hotel
        instance.userManager.createUser(typeUser, name, surname, email, password)
        return cliente
    
class roomManager():
    
    def __init__ (self):
        self.head=None
        
    def is_empty(self):
       return self.head is None
    def add_to_end(self, habitacion):
    
        new_node=Nodo(habitacion)
        if self.is_empty():
            self.head = new_node
            return
        current=self.head
        while current.prox:
            current = current.prox
        current.prox = new_node
    def delete(self, value):
        
        if self.is_empty():
            return

        if self.head.valor == value:
            self.head = self.head.prox
            return

        current = self.head
        while current.prox:
            if current.prox.valor == value:
                current.prox = current.prox.prox
                return
            current = current.prox
    def ocupar_habitacion (self,tipo,bano,balcon,fecha_inicio,fecha_fin):
        current=self.head
        while current.prox: 
            if tipo == current.tipo and current.ocupacion ==False and current.bano==bano and current.balcon==balcon:        
                current.ocuparhabitacion = True 
            current=current.prox                
        print('No hay disponibilidad de la habitacion requerida')
                        
                        
class reservaManager():
    def __init__ (self):
        self.reservas={ }
    def reservar (self, cliente, fecha_inicio, fecha_fin, tipo_habit,balcon,bano):
        reserva=Reserva(cliente, fecha_inicio, fecha_fin, tipo_habit,balcon,bano)
        self.reservas[reserva.nro_reserva]= reserva
