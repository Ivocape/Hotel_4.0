from TiposDeUsuarios import *
from habitacion import *
import datetime
from reservas import *
from buffet import *

class adminManager:
    def __init__(self) -> None:
        self.totalAdmins = []
        self.lista_mails=set()
    
    def createAdmin(self,typeUser ,name, surname, email, password):
        admin = Administrador(name, surname, email, password, typeUser)
        self.totalAdmins.append(admin)
        self.lista_mails.add(email)
        from Index import instance 
        carpeta='users.csv'
        instance.discoHotel1.escribir(carpeta = carpeta,typeUser = typeUser,name = name, surname = surname, email = email, password = password)
        print("Usuario creado con éxito, por favor inicie sesión")
        return admin
    def cache(self,typeUser ,name, surname, email, password):
        admin = Administrador(name, surname, email, password, typeUser)
        self.totalAdmins.append(admin)
        self.lista_mails.add(email)
        return admin
    
class personalManager():
    def __init__(self):
        self.lista_empleado=[] #Yo tengo una lista de empleados(La instancia de personalManager)
        self.lista_tareas=[]
        self.totalPersonal = []
        self.lista_mails=set()     
    def __str__(self) -> str:
        return (str(self.lista_empleado))    
    def createPersonal(self,typeUser ,name, surname, email, password,cargo,tarea): 
        if email in self.lista_mails:
            print('El mail ya esta registrado')
        else:
            personal = Personal(name, surname, email, password, typeUser,cargo,tarea)
            self.lista_empleado.append(personal)
            self.lista_mails.add(email)
            from Index import instance 
            carpeta='users.csv'
            instance.discoHotel1.escribir(carpeta = carpeta,typeUser = typeUser,name = name, surname = surname, email = email, password = password,cargo=cargo,tarea=tarea)
            print("Usuario creado con éxito, por favor inicie sesión")
    def cache(self,typeUser ,name, surname, email, password,cargo,tarea):
        personal = Personal(name, surname, email, password, typeUser,cargo,tarea)
        self.lista_empleado.append(personal)
        self.lista_mails.add(email)
        return personal
 
    def verificacion(self,email,password):
        for personal in self.lista_empleado:
            if  password == personal.password and email== personal.email:
                return True
            return False

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
    def mostrar_personal(self):
        for empleado in self.lista_empleado:
            print(f'{empleado.nombre} - {empleado.apellido} - {empleado.email} - {empleado.cargo}')
    
    
class clienteManager():
    def __init__(self):
        self.lista_cliente=[] 
        self.lista_mails=set()
    def __str__(self) -> str:
        return (str(self.lista_cliente))
    
    def dar_de_baja(self,cliente):
        self.lista_cliente.remove(cliente)
        #Aca necesitamos generar un metodo que elimine al cliente de la lista de clientes en el CSV FALTA yo(abi) no daria de baja
    def createCliente(self,typeUser ,name, surname, email, password):
        cliente = Cliente(name, surname, email, password, typeUser)
        if email in self.lista_mails:
            print('El mail ya esta registrado')
        else:
            self.lista_cliente.append(cliente)
            self.lista_mails.add(email)
            from Index import instance 
            carpeta='users.csv'
            instance.discoHotel1.escribir(carpeta = carpeta,typeUser = typeUser,name = name, surname = surname, email = email, password = password)
            print("Usuario creado con éxito, por favor inicie sesión")

    def cache (self,typeUser ,name, surname, email, password):
        cliente = Cliente(name, surname, email, password, typeUser)
        self.lista_cliente.append(cliente)
        self.lista_mails.add(email)
        return cliente
    def verificacion(self,email,password):
        ######## VALIDACION DE USUARIOS #########
        for cliente in self.lista_cliente:
            
            if  password == cliente.password and email== cliente.email:
                
                return True,cliente.typeUser
        return False,None
    

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
    def crear_habitacion(self,nro_habitacion,tipo,capacidad,precio,bano,balcon):
        habitacion=Habitacion(nro_habitacion,tipo,capacidad,precio,balcon,bano)
        self.add_to_start(habitacion)
        from Index import instance
        carpeta='room.csv'
        instance.discoHotel1.escribir(carpeta = carpeta,nro_habitacion = nro_habitacion,tipo = tipo,capacidad = capacidad,precio = precio,bano = bano,balcon = balcon)      
        
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
                habitacionposible=current.habitacion.nro_habitacion
                for reserva in self.reservas.values():
                    if reserva.nro_habitacion == habitacionposible:
                        if fecha_inicio <= reserva.fecha_inicio <= fecha_fin or fecha_inicio <= reserva.fecha_fin <= fecha_fin:
                            superpuesta = True
                            break
                if not superpuesta:
                    nro_habitacion=current.habitacion.nro_habitacion
                    total=int(current.habitacion.precio)*int(((fecha_fin-fecha_inicio).days+1))
                    nro_reserva=cliente+str(fecha_inicio.date())
                    reserva=Reserva(nro_reserva,cliente, fecha_inicio, fecha_fin, nro_habitacion,total)
                    instance.discoHotel1.escribir(carpeta = 'reservas.csv',nro_reserva = nro_reserva,mail = cliente,nro_habitacion = nro_habitacion,fecha_inicio = fecha_inicio,fecha_fin = fecha_fin,total = total)
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
            current=instance.roomManager.head
            while current is not None:
                if current.habitacion.nro_habitacion == nro_habitacion:
                    current.habitacion.liberarhabitacion()
                    break
                current=current.prox
            del self.reservas[nro_reserva]
            print('La reserva se cancelo con exito')
        else:
            print(f'No existe hay una reserva con el numero {nro_reserva}')
    def mostrar_reservas(self,cliente):
        print('Nro reserva - Fecha inicio - Fecha fin - Precio')
        for reserva in self.reservas.values():
            if reserva.mail == cliente:
                print(f'{reserva.nro_reserva} - {reserva.fecha_inicio} - {reserva.fecha_fin} - ${reserva.total}')
            else:
                print('No hay reservas para el cliente')    
        
    def cache(self,nro_reserva, mail, fecha_inicio, fecha_fin, nro_habitacion,total):
        reserva=Reserva(nro_reserva, mail, fecha_inicio, fecha_fin, nro_habitacion,total)
        self.agregar_reserva(reserva)
        return reserva
                    
