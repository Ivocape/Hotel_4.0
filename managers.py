from TiposDeUsuarios import *
from habitacion import *
import datetime
from collections import deque
from reservas import *
from buffet import *
from tareas import *
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
        instance.discoHotel1.escribir(carpeta = carpeta,typeUser = typeUser,name = name, surname = surname, email = email, password = password,cargo='n/a',tarea='n/a')
        print("Usuario creado con éxito, por favor inicie sesión")
        return admin
    def cache(self,typeUser ,name, surname, email, password):
        admin = Administrador(name, surname, email, password, typeUser)
        self.totalAdmins.append(admin)
        self.lista_mails.add(email)
        return admin
    def verificacion(self,email,password):
        for admin in self.totalAdmins:
            if  password == admin.password and email== admin.email:
                return True, admin.typeUser
            return False, None
    def mostrar_informe(self):
        #porcentaje de ocupacion del hotel
     
        from Index import instance
        current=instance.roomManager.head
        cantidad_habitaciones = 0
        cantidad_habitaciones_ocupadas = 0
        porcentaje_ocupacion = 0
        HabitacionesSuite = 0
        HabitacionesDobles = 0
        HabitacionesSimples = 0
        HabitacionesSuiteOcupadas = 0
        HabitacionesDoblesOcupadas = 0
        HabitacionesSimplesOcupadas = 0

        while current is not None:
            cantidad_habitaciones = cantidad_habitaciones + 1
            if current.habitacion.tipo == "simple":
                HabitacionesSimples = HabitacionesSimples + 1
            elif current.habitacion.tipo == "doble":
                HabitacionesDobles = HabitacionesDobles + 1
            elif current.habitacion.tipo == "suite":
                HabitacionesSuite = HabitacionesSuite + 1

            current=current.prox
        for reserva in instance.reservaManager.reservas_en_lista:
            if datetime.datetime.strptime(reserva.fecha_fin,"%Y-%m-%d %H:%M:%S")>= datetime.datetime.now() and datetime.datetime.strptime(reserva.fecha_inicio,"%Y-%m-%d %H:%M:%S") <= datetime.datetime.now():
                cantidad_habitaciones_ocupadas = cantidad_habitaciones_ocupadas + 1
                if reserva.nro_habitacion.split()[-1][-1] == "C":
                    HabitacionesSimplesOcupadas = HabitacionesSimplesOcupadas + 1
                elif reserva.nro_habitacion.split()[-1][-1] == "B":
                    HabitacionesDoblesOcupadas = HabitacionesDoblesOcupadas + 1
                elif reserva.nro_habitacion.split()[-1][-1] == "A":
                    HabitacionesSuiteOcupadas = HabitacionesSuiteOcupadas + 1

        porcentaje_ocupacion = (cantidad_habitaciones_ocupadas/cantidad_habitaciones)*100
        porcentaje_ocupacion_simples = (HabitacionesSimplesOcupadas/HabitacionesSimples)*100
        porcentaje_ocupacion_dobles = (HabitacionesDoblesOcupadas/HabitacionesDobles)*100
        porcentaje_ocupacion_suite = (HabitacionesSuiteOcupadas/HabitacionesSuite)*100

        print("El porcentaje de ocupacion es de: " + str(porcentaje_ocupacion) + "%")
        print("El porcentaje de ocupacion de habitaciones simples es de: " + str(porcentaje_ocupacion_simples) + "%")
        print("El porcentaje de ocupacion de habitaciones dobles es de: " + str(porcentaje_ocupacion_dobles) + "%")
        print("El porcentaje de ocupacion de habitaciones suite es de: " + str(porcentaje_ocupacion_suite) + "%")

        return porcentaje_ocupacion, porcentaje_ocupacion_simples, porcentaje_ocupacion_dobles, porcentaje_ocupacion_suite
     
        #porcentaje de ocupacion de habitaciones por tipo de habitacion
    def informe_recaudacion_diaria(self,fecha):
        from Index import instance
        recaudacion = 0
        for reserva in instance.reservaManager.reservas_en_lista:
            if reserva.fecha_reserva.date() == fecha.date():
                recaudacion = recaudacion + reserva.total
        for pedido in instance.buffet.lista_pedidos:
            if pedido[4].date() == fecha.date():
                recaudacion = recaudacion + pedido[3]
        print("La recaudacion diaria es de: " + str(recaudacion))
        return recaudacion    
    

class personalManager():
    def __init__(self):
        self.lista_empleado=[] #Yo tengo una lista de empleados(La instancia de personalManager)
        self.lista_tareas=deque() #Yo tengo una lista de tareas
        
        self.registros=[]
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
                return True, personal.typeUser
            return False, None

    def dar_de_baja(self,inputbaja):
        for empleado in self.lista_empleado:
            if empleado.email == inputbaja:
                self.lista_empleado.remove(empleado)
                print(f'Empleado {inputbaja} dado de baja con exito')
                break
        from Index import instance
        instance.discoHotel1.eliminar_personal(inputbaja)
    def nuevatarea(self,tarea,cargo):
        tarea=Tarea(tarea,cargo)
        self.lista_tareas.append(tarea)
        from Index import instance
        instance.discoHotel1.escribir(carpeta = 'tareas.csv',tarea = tarea.tarea,cargo = tarea.cargo)
        
    def completar_tarea(self,email):
        for empleado in self.lista_empleado:
            if empleado.email == email:
                empleado.tarea=''
                from Index import instance
                instance.discoHotel1.completar_tarea(email)
                print('Tarea completada con exito')
                break
        
    def asignacion_tareas(self,email): #Asignarle una tarea a un determinado empleado y Guardarla en el CSV
        for user in self.lista_empleado:
            if user.email == email and user.tarea == '':
                for i in self.lista_tareas:
                        if user.cargo==i.cargo:
                            
                            user.tarea=i.tarea
                            self.lista_tareas.popleft()
                            from Index import instance
                            instance.discoHotel1.asignar_tarea(email,user.tarea)
                            instance.discoHotel1.eliminar_tarea(user.tarea)
                            print(f'Tarea {user.tarea} asignada con exito')
                            break
                        else:
                            print('No hay tareas disponibles para el cargo')
            else:
                print('El empleado ya tiene una tarea asignada')
    def cache_tarea(self,tarea,cargo):
        tarea=Tarea(tarea,cargo)
        self.lista_tareas.append(tarea)
        return tarea
    
    def mostrar_tareas(self):
        print('Tareas disponibles:')
        for tarea in self.lista_tareas:
            print(f'{tarea.tarea} - {tarea.cargo}')

    def asignacion_tareas_todos(self): #Asignarle tareas a todos
        for empleado in self.lista_empleado:
            if empleado.tarea == '':
                for tarea in self.lista_tareas:
                    if empleado.cargo==tarea.cargo:
                        empleado.tarea=tarea.tarea
                        self.lista_tareas.popleft()
                        from Index import instance
                        instance.discoHotel1.asignar_tarea(empleado.email,empleado.tarea)
                        instance.discoHotel1.eliminar_tarea(empleado.tarea)
                        print(f'Tarea {empleado.tarea} asignada con exito')
                        break
                    else:
                        print('No hay tareas disponibles para el cargo')
           
    def ingresos_cache(self,movimiento, mail,fecha):
        self.registros.append([movimiento,mail,fecha])    
    def registrar_ingreso(self,empleado):
        self.registros.append(['Ingreso',empleado,datetime.datetime.now()])
        from Index import instance
        instance.discoHotel1.escribir(carpeta = 'ingresos.csv',movimiento = 'Ingreso',mail = empleado,fecha = datetime.datetime.now())
    def registrar_egreso(self,empleado):
        self.registros.append(['Egreso',empleado,datetime.datetime.now()])
        from Index import instance  
        instance.discoHotel1.escribir(carpeta = 'ingresos.csv',movimiento = 'Egreso',mail = empleado,fecha = datetime.datetime.now())
    def mostrar_ingresos(self):
        print('Movimiento - Mail - Fecha')
        for registro in self.registros:
            print(f'{registro[0]} - {registro[1]} - {registro[2]}')
    def mostrar_personal(self):
        for empleado in self.lista_empleado:
            print(f'{empleado.name} - {empleado.surname} - {empleado.email} - {empleado.cargo}')
    
    
class clienteManager():
    def __init__(self):
        self.lista_cliente=[] 
        self.lista_mails=set()
        
    def __str__(self) -> str:
        return (str(self.lista_cliente))
    
    def createCliente(self,typeUser ,name, surname, email, password):
        cliente = Cliente(name, surname, email, password, typeUser)
        if email in self.lista_mails:
            print('El mail ya esta registrado')
        else:
            self.lista_cliente.append(cliente)
            self.lista_mails.add(email)
            from Index import instance 
            carpeta='users.csv'
            instance.discoHotel1.escribir(carpeta = carpeta,typeUser = typeUser,name = name, surname = surname, email = email, password = password,cargo='n/a',tarea='n/a')
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

    
    def reservar(self, email, fecha_inicio,fecha_fin, tipo_habit,bano,balcon):
        from Index import instance
        total=instance.reservaManager.reservar(email, fecha_inicio,fecha_fin, tipo_habit,balcon,bano)
        for cliente in self.lista_cliente:
            if cliente.email == email:
                cliente.apilar(total)
                instance.discoHotel1.escribir(carpeta = 'inversion.csv',mail = email,gasto=total)
                break
    
    def pedir_comida(self, email, alimento, cant_pedida):
        from Index import instance
        a=instance.buffet.tomar_pedido(email, alimento, cant_pedida)
        for cliente in self.lista_cliente:
            if cliente.email == email:
                cliente.apilar(a)
                instance.discoHotel1.escribir(carpeta = 'inversion.csv',mail = email,gasto=a)
                break
    
    def inversion_cache(self, mail,gasto):
        for cliente in self.lista_cliente:
            if cliente.email == mail:
                cliente.apilar(gasto)
                break
            
    def gastosclientes(self):
        for cliente in self.lista_cliente:
            print(f'{cliente.email} - {cliente.calcultar_total()} ')


class roomManager():
    
    def __init__ (self):
        self.head=None
        
    def is_empty(self):
       return self.head is None
    def add_to_start(self, habitacion):
    
        new_node=Nodo(habitacion)
        new_node.prox = self.head
        self.head = new_node
      
        
            
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
        self.reservas_en_lista=[]
    def agregar_reserva(self,reserva):
        self.reservas[reserva.nro_reserva]= reserva
        self.reservas_en_lista.append(reserva)
        
    def reservar (self, cliente, fecha_inicio,fecha_fin, tipo_habit,balcon,bano):
        

        from Index import instance
        current=instance.roomManager.head
        
        while current is not None:
            if tipo_habit == current.habitacion.tipo and  current.habitacion.ocupacion==False and bano == current.habitacion.bano and balcon == current.habitacion.balcon:
                superpuesta = False
                habitacionposible=current.habitacion.nro_habitacion
                for reserva in self.reservas.values():
                    if reserva.nro_habitacion == habitacionposible:
                        if fecha_inicio <= datetime.datetime.strptime(reserva.fecha_inicio,"%Y-%m-%d %H:%M:%S") <= fecha_fin or fecha_inicio <= datetime.datetime.strptime(reserva.fecha_fin,"%Y-%m-%d %H:%M:%S") <= fecha_fin:
                            superpuesta = True
                            break
                if not superpuesta:
                    nro_habitacion=current.habitacion.nro_habitacion
                    total=int(current.habitacion.precio)*int(((fecha_fin-fecha_inicio).days+1))
                    nro_reserva=cliente+str(fecha_inicio.date())
                    reserva=Reserva(nro_reserva,cliente, fecha_inicio, fecha_fin, nro_habitacion,total,datetime.datetime.now())
                    instance.discoHotel1.escribir(carpeta = 'reservas.csv',nro_reserva = nro_reserva,mail = cliente,nro_habitacion = nro_habitacion,fecha_inicio = fecha_inicio,fecha_fin = fecha_fin,total = total,fecha_reserva = datetime.datetime.now())
                    self.agregar_reserva(reserva)
                    current.habitacion.ocuparhabitacion()
                    
                    print(f'La reserva se realizo con exito, su numero de reserva es {reserva.nro_reserva} con un costo de {reserva.total}')
                    return total
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
        flag=False
        print('Nro reserva - Fecha inicio - Fecha fin - Precio')
        for reserva in self.reservas.values():
            if reserva.mail == cliente:
                flag=True
                print(f'{reserva.nro_reserva} - {reserva.fecha_inicio} - {reserva.fecha_fin} - ${reserva.total}')
        if flag==False:
            print('No hay reservas para el cliente')    
        
    def cache(self,nro_reserva, mail, fecha_inicio, fecha_fin, nro_habitacion,total,fecha_reserva):
        reserva=Reserva(nro_reserva, mail, fecha_inicio, fecha_fin, nro_habitacion,total,fecha_reserva)
        self.agregar_reserva(reserva)
        return reserva
                    
