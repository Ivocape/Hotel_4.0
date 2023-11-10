import csv
import pandas as pd
#####################################################################################
# ESTE DISCO DURO DEBE DE ENCARGARSE DE GUARDAR TODA INFORMACION DE USUARIOS, CLIENTES, PERSONAL, ADMINS,
#####################################################################################
class DiscoDuro():
    # Create a list to store the user information
    def __init__(self) -> None:
        pass

    def leerSETUP (self, carpeta):    
        # Open the CSV file
        with open(carpeta,'r', newline='') as csvfile: 
            # Create a CSV reader object
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            match carpeta:
                case "users.csv":
                            # Loop through each row in the CSV file
                    for row in reader:
                        # Extract the user information from the row
                        
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
                        # Extract the user information from the row
                        nro_reserva = row[0]
                        mail = row[1]
                        nro_habitacion = row[4]
                        fecha_inicio = row[2]
                        fecha_fin = row[3]
                        total = row[5]
                        
                        from Index import instance
                        instance.reservaManager.cache(nro_reserva, mail, fecha_inicio, fecha_fin, nro_habitacion,total)
                case 'room.csv':
                    #numero de habitacion, tipo, capacidad, baño, balcon, precio de la noche
                    #nro_habitacion,tipo,capacidad,precio,bano,balcon
                             # Loop through each row in the CSV file
                    for row in reader:
                        # Extract the user information from the row
                        
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

                            

    def escribir (self, carpeta, **kwargs):
        #Aca importamos la instancia de la clase Hotel
        match carpeta:
            case 'users.csv':
                # Open the CSV file in append mode
                #instance.clienteManager.createCliente(kwargs["typeUser"],kwargs['name'], kwargs['surname'], kwargs['email'],kwargs['password'])
                
                with open('users.csv', 'a', newline='') as csvfile:
                    # Create a CSV writer object
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    #quiero diferenciar segun el tipo de usuario
                    if kwargs["typeUser"] == "personal 1234":
                        writer.writerow([kwargs['name'], kwargs['surname'], kwargs['email'],kwargs['password'],kwargs["typeUser"],kwargs['cargo'],kwargs['tarea']])
                    else:
                    # Write the user information to the CSV file
                        writer.writerow([kwargs['name'], kwargs['surname'], kwargs['email'],kwargs['password'],kwargs["typeUser"]])
            case 'reservas.csv':
                with open('reservas.csv', 'a', newline='') as csvfile:
                    # Create a CSV writer object
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Write the user information to the CSV file
                    writer.writerow([kwargs['nro_reserva'], kwargs['mail'],kwargs['fecha_inicio'],kwargs['fecha_fin'],kwargs['nro_habitacion'],kwargs['total']])
            case 'room.csv':
                with open('room.csv', 'a', newline='') as csvfile:
                    # Create a CSV writer object
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Write the user information to the CSV file
                    writer.writerow([kwargs['nro_habitacion'], kwargs['tipo'],kwargs['capacidad'],kwargs['precio'],kwargs['baño'],kwargs['balcon']])
            case 'buffet.csv':
                with open('buffet.csv', 'a', newline='') as csvfile:
                    # Create a CSV writer object
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Write the user information to the CSV file
                    writer.writerow([kwargs['alimento'], kwargs['precio'],kwargs['cant']])
            case 'tareas.csv':
                with open('tareas.csv', 'a', newline='') as csvfile:
                    # Create a CSV writer object
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Write the user information to the CSV file
                    writer.writerow([kwargs['tarea'], kwargs['cargo']])

            
    def eliminar_personal(self, inputbaja):
            df=pd.read_csv('users.csv')
            df=df[df['email']!= inputbaja]
            df.to_csv('users.csv',index=False)
    def eliminar_alimento(self, inputbaja):
            df=pd.read_csv('buffet.csv')
            df=df[df['alimento']!= inputbaja]
            df.to_csv('buffet.csv',index=False)
