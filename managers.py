from TiposDeUsuarios import *


class userManager:
    def __init__(self) -> None:
        self.totalUsers = [] ######### Aca Vamos a tener un problema #####
    def mostrarlista(self):
        print(self.totalUsers)
    # Returns a new instantiation of the User Class for storage in a variable
    # Instantiations can be accessed later by accessing the __totalUsers array
    def cacheUser(self, typeUser ,name, surname, email, password):
        user = User(typeUser,name, surname, email, password)
        self.totalUsers.append(user)

        print ("cache sumado")
        print(self.totalUsers)  
        if typeUser == "admin 1234":
            admin = Administrador(name, surname, email, password)
            from Index import instance
            instance.adminManager.totalAdmins.append(admin)
        elif typeUser == "cliente":
            cliente = Cliente(name, surname, email, password)
            from Index import instance 
            instance.clienteManager.lista_cliente.append(cliente)
            
        elif typeUser == "personal 1234":
            personal = Personal(name, surname, email, password)
            from Index import instance 
            instance.personalManager.totalPersonal.append(personal)

        return user
    def createUser(self, typeUser ,name, surname, email, password):
        user = User(typeUser,name, surname, email, password)
        self.totalUsers.append(user)
        print(self.totalUsers)
        print(self)
        from Index import instance 
        instance.discoHotel1.escribir(typeUser,name, surname, email, password)
        
        return self.totalUsers

    # Validates the password of a specific user against a preset password
    # This will return  if the password is valid and False if it is not
    def validateUser(self,email, password):
        #aca tengo que hacer un for para leer una lista de usuarios y encontrar el usuario que quiero. luego comparar las contraseñas.
        from Index import instance
        for user in instance.discoHotel1.users:
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

class adminManager:
    def __init__(self) -> None:
        self.totalAdmins = []
    
    def createAdmin(self,typeUser ,name, surname, email, password):
        admin = Administrador(name, surname, email, password)
        self.totalAdmins.append(admin)
        from Index import instance 
        instance.discoHotel1.escribir(typeUser,name, surname, email, password)
        return admin
    def cache(self,typeUser ,name, surname, email, password):
        admin = Administrador(name, surname, email, password)
        self.totalAdmins.append(admin)
        return admin
    
class personalManager():
    def __init__(self):
        self.lista_empleado=[] #Yo tengo una lista de empleados(La instancia de personalManager)
        self.lista_tareas=[]
        self.totalPersonal = []         
    def createPersonal(self,typeUser ,name, surname, email, password): 
     
        personal = Personal(name, surname, email, password)
        self.totalPersonal.append(personal)
        from Index import instance 
        instance.discoHotel1.escribir(typeUser,name, surname, email, password)
    def cache(self,typeUser ,name, surname, email, password):
        personal = Personal(name, surname, email, password)
        self.totalPersonal.append(personal)
        return personal

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
        from Index import instance 
        instance.discoHotel1.escribir(typeUser,name, surname, email, password)
    
    def cache (self,typeUser ,name, surname, email, password):
        cliente = Cliente(name, surname, email, password)
        self.lista_cliente.append(cliente)
        print(self.lista_cliente)
        print(cliente.name)
        return cliente
    
class roomManager():
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
                        
                        
class reservaManager():
    def __init__ (self):
        self.reservas={ }
    def agregar_reserva (self, reserva):
        self.reservas[reserva.nro_reserva]= reserva