from TiposDeUsuarios import *
from habitacion import *
import datetime
from reservas import *
from buffet import *

# class userManager:
#     def __init__(self) -> None:
#         self.totalUsers = [] ######### Aca Vamos a tener un problema #####
#     def mostrarlista(self):
#         print(self.totalUsers)
#     # Returns a new instantiation of the User Class for storage in a variable
#     # Instantiations can be accessed later by accessing the __totalUsers array
#     def cacheUser(self, typeUser ,name, surname, email, password):
#         user = User(typeUser,name, surname, email, password)
#         self.totalUsers.append(user)

#         print ("cache sumado")
#         print(self.totalUsers)  
#         if typeUser == "admin 1234":
#             admin = Administrador(name, surname, email, password)
#             from Index import instance
#             instance.adminManager.totalAdmins.append(admin)
#         elif typeUser == "cliente":
#             cliente = Cliente(name, surname, email, password)
#             from Index import instance 
#             instance.clienteManager.lista_cliente.append(cliente)
            
#         elif typeUser == "personal 1234":
#             personal = Personal(name, surname, email, password)
#             from Index import instance 
#             instance.personalManager.totalPersonal.append(personal)

#         return user
#     def createUser(self, typeUser ,name, surname, email, password):
#         user = User(typeUser,name, surname, email, password)
#         self.totalUsers.append(user)
#         print(self.totalUsers)
#         print(self)
#         from Index import instance 
#         instance.discoHotel1.escribir(typeUser,name, surname, email, password) #NO LO VAMOS A USAR MAS NO CAMBIAR CSV
        
#         return self.totalUsers

    # # Validates the password of a specific user against a preset password
    # # This will return  if the password is valid and False if it is not
    # def validateUser(self,email, password):
    #     #aca tengo que hacer un for para leer una lista de usuarios y encontrar el usuario que quiero. luego comparar las contraseñas.
    #     from Index import instance
    #     for user in instance.discoHotel1.users:
    #         if user['email'] == email:    
    #             if password == user['password']:
    #                 print ("Bienvenido, usted ha ingresado correctamente al sistema")
    #                 return True
    #             else:
    #                 print("La contraseña es incorrecta")
    #                 return False
    #         else:
    #             print("El usuario no existe")
    #             return False

class adminManager:
    def __init__(self) -> None:
        self.totalAdmins = []
    
    def createAdmin(self,typeUser ,name, surname, email, password):
        admin = Administrador(name, surname, email, password, typeUser)
        self.totalAdmins.append(admin)
        from Index import instance 
        carpeta='users.csv'
        instance.discoHotel1.escribir(carpeta = carpeta,typeUser = typeUser,name = name, surname = surname, email = email, password = password)
        return admin
    def cache(self,typeUser ,name, surname, email, password):
        admin = Administrador(name, surname, email, password, typeUser)
        self.totalAdmins.append(admin)
        return admin
    
class personalManager():
    def __init__(self):
        self.lista_empleado=[] #Yo tengo una lista de empleados(La instancia de personalManager)
        self.lista_tareas=[]
        self.totalPersonal = []     
    def __str__(self) -> str:
        return (str(self.lista_empleado))    
    def createPersonal(self,typeUser ,name, surname, email, password): 
     
        personal = Personal(name, surname, email, password, typeUser)
        self.lista_empleado.append(personal)
        from Index import instance 
        carpeta='users.csv'
        instance.discoHotel1.escribir(carpeta = carpeta,typeUser = typeUser,name = name, surname = surname, email = email, password = password)
    def cache(self,typeUser ,name, surname, email, password):
        personal = Personal(name, surname, email, password, typeUser)
        self.lista_empleado.append(personal)
        return personal
 
    def verificacion(self,email,password):
        for personal in self.lista_empleado:
            if  password == personal.password and email== personal.email:
                return True
            return False
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
    def __str__(self) -> str:
        return (str(self.lista_cliente))
    
    def dar_de_baja(self,cliente):
        self.lista_cliente.remove(cliente)
        #Aca necesitamos generar un metodo que elimine al cliente de la lista de clientes en el CSV FALTA yo(abi) no daria de baja
    def createCliente(self,typeUser ,name, surname, email, password):
        cliente = Cliente(name, surname, email, password, typeUser)
        self.lista_cliente.append(cliente)
        from Index import instance 
        carpeta='users.csv'
        instance.discoHotel1.escribir(carpeta = carpeta,typeUser = typeUser,name = name, surname = surname, email = email, password = password)
  
    def cache (self,typeUser ,name, surname, email, password):
        cliente = Cliente(name, surname, email, password, typeUser)
        self.lista_cliente.append(cliente)
        return cliente
    def verificacion(self,email,password):
        ######## VALIDACION DE USUARIOS #########
        for cliente in self.lista_cliente:

            if  password == cliente.password and email== cliente.email:
                
                return True
            return False
    
    def reservar (self, cliente, año_inicio, mes_inicio,dia_inicio, año_fin,mes_fin,dia_fin, tipo_habit,balcon,bano): #CHEQUEAR SI SE PUEDE VINCULAR EL USUARIO CON LA RESERVA #############################################
        fecha_inicio=datetime.datetime(año_inicio,mes_inicio,dia_inicio,15,0)
        fecha_fin=datetime.datetime(año_fin,mes_fin,dia_fin,10,0)
        from Index import instance
        instance.reservaManager.reservar(cliente,fecha_inicio, fecha_fin, tipo_habit,balcon,bano)
    def pedir_comida(self, cliente, alimento, cant_pedida):
        from Index import instance
        instance.buffet.tomar_pedido(cliente, alimento, cant_pedida)
    

class roomManager():
    
    def __init__ (self):
        self.head=None
        
    def is_empty(self):
       return self.head is None
    def add_to_start(self, habitacion):
    
        new_node=Nodo(habitacion)
        new_node.prox = self.head
        self.head = new_node
       
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
            
    def ocupar_habitacion (self,nro_habitacion):
        current=self.head
        while current is not None: 
            if current.habitacion-nro_habitacion == nro_habitacion:
                if current.habitacion.ocupacion == True:
                    print(f'la habitacion {nro_habitacion} ya esta ocupada')
                else:
                    current.habitacion.ocuparhabitacion()
                return
            current=current.prox
            
    def liberar_habitacion(self,nro_habitacion):
        current=self.head
        while current is not None:
            if current.habitacion.nro_habitacion == nro_habitacion:
                if current.habitacion.ocupacion:
                    current.habitacion.liberar_habitacion()
                else:
                    print('La habitacion no esta ocupada')
                return
            current=current.prox
            
    def mostrar_habitaciones(self):
        current=self.head
        print('Habitaciones disponibles:')
        print('Nro habitacion - Tipo - Capacidad - Precio - Baño - Balcon')
        while current is not None:
            print(f'{current.habitacion.nro_habitacion} - {current.habitacion.tipo} - {current.habitacion.capacidad} - {current.habitacion.precio} - {current.habitacion.bano} - {current.habitacion.balcon}')
            current=current.prox
    def cache(self,nro_habitacion,tipo,capacidad,precio,bano,balcon):
        habitacion=Habitacion(nro_habitacion,tipo,capacidad,precio,balcon,bano)
        self.add_to_start(habitacion)               
                          
                        
                        
class reservaManager():
    def __init__ (self):
        self.reservas={ }
    def agregar_reserva(self,reserva):
        self.reservas[reserva.nro_reserva]= reserva
        
    def reservar (self, cliente, fecha_inicio,fecha_fin, tipo_habit,balcon,bano):
        

        from Index import instance
        current=instance.roomManager.head
        
        while current is not None:
            if tipo_habit == current.habitacion.tipo and  current.habitacion.ocupacion==False and bano == current.habitacion.bano and balcon == current.habitacion.balcon:
                superpuesta = False
                for reserva in self.reservas.values():
                    if (
                        reserva.tipo_habit == tipo_habit
                        and bano == reserva.bano
                        and balcon == reserva.balcon
                        and (
                            (fecha_inicio >= reserva.fecha_inicio and fecha_inicio <= reserva.fecha_fin)
                            or (fecha_fin >= reserva.fecha_inicio and fecha_fin <= reserva.fecha_fin)
                        )
                    ):
                        superpuesta = True
                        break
                if not superpuesta:
                    reserva=Reserva(cliente, fecha_inicio, fecha_fin, tipo_habit,balcon,bano)
                    reserva.total=int(current.habitacion.precio)*int(((fecha_fin-fecha_inicio).days+1))
                    reserva.nro_habitacion=current.habitacion.nro_habitacion
                    self.agregar_reserva(reserva)
                    current.habitacion.ocuparhabitacion()
                    
                    print(f'La reserva se realizo con exito, su numero de reserva es {reserva.nro_reserva} con un costo de {reserva.total}')
                    return
            current=current.prox
            
        print(f'No hay habitaciones disponibles para el tipo {tipo_habit} con las caracteristicas solicitadas')
        
    def cancelar_reserva(self,nro_reserva):
        if nro_reserva in self.reservas:
            from Index import instance
            reserva = self.reservas[nro_reserva]
            nro_habitacion = reserva.nro_habitacion
            current=instance.roomManager.habitaciones.head
            while current is not None:
                if current.habitacion.nro_habitacion == nro_habitacion:
                    current.habitacion.liberarhabitacion()
                    break
                current=current.prox
        del self.reservas[nro_reserva]
        print('La reserva se cancelo con exito')

    def mostrar_reservas(self,cliente):
        print('Nro reserva - Fecha inicio - Fecha fin - Precio')
        for reserva in self.reservas.values():
            if reserva.mail == cliente:
                print(f'{reserva.nro_reserva} - {reserva.fecha_inicio} - {reserva.fecha_fin} - ${reserva.total}')
            else:
                print('No hay reservas para el cliente')    
            
                    
