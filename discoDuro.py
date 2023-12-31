import csv
import pandas as pd
import datetime
#####################################################################################
# ESTE DISCO DURO DEBE DE ENCARGARSE DE GUARDAR TODA INFORMACION DE USUARIOS, CLIENTES, PERSONAL, ADMINS,
#####################################################################################
class DiscoDuro():
    # Crear el disco duro
    def __init__(self) -> None:
        pass

    def leerSETUP (self, carpeta):    
        # Abrir el archivo CSV
        with open(carpeta,'r', newline='') as csvfile: 
            # Crear un objeto lector CSV
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            match carpeta:
                case "users.csv":
                            
                    for row in reader:
                        # Extraigo la informacion del usuario de la fila
                        
                        name = row[0]
                        surname = row[1]
                        email = row[2]
                        password = row[3]
                        typeUser = row[4]
                        from Index import instance #Aca importamos la instancia de la clase Hotel 
                        if typeUser == "admin 1234":
                            instance.adminManager.cache(typeUser,name, surname, email, password)
                        elif typeUser == "cliente":
                            instance.clienteManager.cache(typeUser,name, surname, email, password)
                        elif typeUser == "personal 1234":
                            cargo=row[5]
                            tarea=row[6]
                            instance.personalManager.cache(typeUser,name, surname, email, password,cargo,tarea)
                          
                    
                 
                case 'reservas.csv':
                 
                    for row in reader:
                        # Extraigo la informacion de la reserva de la fila
                        nro_reserva = row[0]
                        mail = row[1]
                        nro_habitacion = row[4]
                        fecha_inicio = row[2]
                        fecha_fin = row[3]
                        total = int(row[5])
                        fecha_reserva = datetime.datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S.%f')
                        
                        from Index import instance
                        instance.reservaManager.cache(nro_reserva, mail, fecha_inicio, fecha_fin, nro_habitacion,total,fecha_reserva)
                case 'room.csv':
                    
                             
                    for row in reader:
                        # Extraigo la informacion de la habitacion de la fila
                        
                        nro_habitacion = row[0]
                        tipo = row[1]
                        capacidad = row[2]
                        precio= row[3]
                        baño = row[4]
                        balcon = row[5] 

                        from Index import instance
                        instance.roomManager.cache(nro_habitacion,tipo,capacidad,precio,baño,balcon)
                case 'buffet.csv':
                    for row in reader:
                        alimento = row[0]
                        precio = row[1]
                        cant = row[2]
                        from Index import instance
                        instance.buffet.cache(alimento, precio, cant)
                case 'tareas.csv':
                    for row in reader:
                        tarea = row[0]
                        cargo = row[1]
                        from Index import instance
                        instance.personalManager.cache_tarea(tarea, cargo)
                case 'pedidos.csv':
                    for row in reader:
                        cliente = row[0]
                        alimento = row[1]
                        cant_pedida = row[2]
                        total = row[3]
                        fecha = row[4]
                        from Index import instance
                        instance.buffet.cache_pedidos(cliente, alimento, cant_pedida, total, fecha)
                case 'ingresos.csv':
                    for row in reader:
                        movimiento = row[0]
                        mail = row[1]
                        fecha = row[2]
                        from Index import instance
                        instance.personalManager.ingresos_cache(movimiento, mail,fecha)
                case 'inversion.csv':
                    for row in reader:
                        mail = row[0]
                        
                        gasto = row[1]
                        fecha = row[2]
                        
                        from Index import instance
                        instance.clienteManager.inversion_cache(mail,gasto,fecha)
                            

    def escribir (self, carpeta, **kwargs):
        #Aca importamos la instancia de la clase Hotel
        match carpeta:
            case 'users.csv':
                
                
                with open('users.csv', 'a', newline='') as csvfile:
                    # Crear un objeto escritor CSV
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    #Escrebir la informacion del usuario en el archivo CSV
                    writer.writerow([kwargs['name'], kwargs['surname'], kwargs['email'],kwargs['password'],kwargs["typeUser"],kwargs['cargo'],kwargs['tarea']])

            case 'reservas.csv':
                with open('reservas.csv', 'a', newline='') as csvfile:
                    # Crear un objeto escritor CSV
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Escribir la informacion del usuario en el archivo CSV
                    writer.writerow([kwargs['nro_reserva'], kwargs['mail'],kwargs['fecha_inicio'],kwargs['fecha_fin'],kwargs['nro_habitacion'],kwargs['total'],kwargs['fecha_reserva']])
            case 'room.csv':
                with open('room.csv', 'a', newline='') as csvfile:
                    # CCrear un objeto escritor CSV
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Escrbir la informacion del usuario en el archivo CSV
                    writer.writerow([kwargs['nro_habitacion'], kwargs['tipo'],kwargs['capacidad'],kwargs['precio'],kwargs['baño'],kwargs['balcon']])
            case 'buffet.csv':
                with open('buffet.csv', 'a', newline='') as csvfile:
                    # Crear un objeto escritor CSV
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Escrbir la informacion del usuario en el archivo CSV
                    writer.writerow([kwargs['alimento'], kwargs['precio'],kwargs['cant']])
            case 'tareas.csv':
                with open('tareas.csv', 'a', newline='') as csvfile:
                    # Crear un objeto escritor CSV
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Escribir la informacion del usuario en el archivo CSV
                    writer.writerow([kwargs['tarea'], kwargs['cargo']])
            case 'pedidos.csv':
                with open('pedidos.csv', 'a', newline='') as csvfile:
                    # Crear un objeto escritor CSV
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # escribir la informacion del usuario en el archivo CSV
                    writer.writerow([kwargs['cliente'], kwargs['alimento'],kwargs['cant_pedida'],kwargs['total'],kwargs['fecha']])
            case 'ingresos.csv':
                with open('ingresos.csv', 'a', newline='') as csvfile:
                    # Crear un objeto escritor CSV
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Escribir la informacion del usuario en el archivo CSV
                    writer.writerow([kwargs['movimiento'], kwargs['mail'],kwargs['fecha']])
            case 'inversion.csv':
                with open('inversion.csv', 'a', newline='') as csvfile:
                    # Crear un objeto escritor CSV
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Escribir la informacion del usuario en el archivo CSV
                    writer.writerow([kwargs['mail'],kwargs['gasto'],kwargs['fecha']])

    #ACTUALIZACION CSV DE USUARIOS CON LAS TAREAS        
    def eliminar_personal(self, inputbaja):
            df=pd.read_csv('users.csv',header=None)
            df=df[df[2]!= inputbaja]
            df.to_csv('users.csv',index=False,header=None)
    def completar_tarea(self, mail):
            df=pd.read_csv('users.csv',header=None)
            df.loc[df.iloc[:, 2] ==mail,6]=''
            df.to_csv('users.csv',index=False,header=None)
            
    def asignar_tarea(self, inputbaja,tarea):
            df=pd.read_csv('users.csv',header=None)
            df[2]=df[2].astype(str)
            df.loc[df[2]==inputbaja,6]=tarea
            df.to_csv('users.csv',index=False,header=None)
    
    #ACTUALIZACION CSV DE TAREAS ELIMINANDO LAS ASIGNADAS        
    def eliminar_tarea(self, tarea):
            df=pd.read_csv('tareas.csv',header=None)
            df=df[df[0]!= tarea]
            df.to_csv('tareas.csv',index=False,header=None)
    
    #ACTUALIZACION CSV DE BUFFET
    def eliminar_alimento(self, inputbaja):
            df=pd.read_csv('buffet.csv',header=None)
            df=df[df[0]!= inputbaja]
            df.to_csv('buffet.csv',index=False,header=None)
    def cambiar_precio_comida(self,alimento,precio):
        df=pd.read_csv('buffet.csv',header=None)
        df.loc[df[0]==alimento,1]=precio
        df.to_csv('buffet.csv',index=False, header=None)
    def reponer_cant (self, alimento, cant):
        df=pd.read_csv('buffet.csv',header=None)
        df.loc[df[0]==alimento,2]=cant
        df.to_csv('buffet.csv',index=False, header=None)    
    
    #ELIMINAR RESERVA CANCELADA
    def eliminar_reserva(self, nro_reserva):
            df=pd.read_csv('reservas.csv',header=None)
            df=df[df[0]!= nro_reserva]
            df.to_csv('reservas.csv',index=False,header=None)