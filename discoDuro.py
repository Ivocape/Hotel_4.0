import csv
#####################################################################################
# ESTE DISCO DURO DEBE DE ENCARGARSE DE GUARDAR TODA INFORMACION DE USUARIOS, CLIENTES, PERSONAL, ADMINS,
#z
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
                            instance.personalManager.cache(typeUser,name, surname, email, password)
                          
                    
                    # # Print the user information
                    # for user in instance.userManager.totalUsers:
                    #     print(user.name, user.surname, user.email, user.password, user.typeUser)
                    #     print ("-------------------------------------------------------------------------")

                case 'reservas.csv':
                    #numero de reserva, cliente, numero de habitacion, numero de reserva, fecha de inicio, fecha de fin, precio total
                    #nro_reserva,mail,nro_habitacion,fecha_inicio,fecha_fin,total
                    # Loop through each row in the CSV file

                    for row in reader:
                        # Extract the user information from the row
                        nro_reserva = row[0]
                        mail = row[1]
                        nro_habitacion = row[2]
                        fecha_inicio = row[3]
                        fecha_fin = row[4]
                        total = row[5]
                        balcon = row[6]
                        bano = row[7]
                        from Index import instance
                        instance.reservaManager.cache(nro_reserva,mail,nro_habitacion,fecha_inicio,fecha_fin,total,balcon,bano)
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
                    pass
                case 'buffet.csv':
                      #menu, precio, stock 
                      pass


    def escribir (self, carpeta, **kwargs):
        #Aca importamos la instancia de la clase Hotel
        match carpeta:
            case 'users.csv':
                # Open the CSV file in append mode
                #instance.clienteManager.createCliente(kwargs["typeUser"],kwargs['name'], kwargs['surname'], kwargs['email'],kwargs['password'])
                
                with open('users.csv', 'a', newline='') as csvfile:
                    # Create a CSV writer object
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    
                    # Write the user information to the CSV file
                    writer.writerow([kwargs['name'], kwargs['surname'], kwargs['email'],kwargs['password'],kwargs["typeUser"]])
            case 'reservas.csv':
                with open('reservas.csv', 'a', newline='') as csvfile:
                    # Create a CSV writer object
                    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    # Write the user information to the CSV file
                    writer.writerow([kwargs['nro_reserva'], kwargs['mail'], kwargs['nro_habitacion'],kwargs['fecha_inicio'],kwargs['fecha_fin'],kwargs['total']])
            case 'room.csv':
                pass
            case 'buffet.csv':
                pass


