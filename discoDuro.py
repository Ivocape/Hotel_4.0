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
                        # Add the user information to the list
                        from Index import instance 
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
                    pass
                case 'room.csv':
                    #numero de habitacion, tipo, baño, balcon, precio de la noche
                    pass
                case 'buffet.csv':
                      #menu, precio, stock 
                      pass


    def escribir (self, carpeta, **kwargs):
        from Index import instance #Aca importamos la instancia de la clase Hotel
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
                pass
            case 'room.csv':
                pass
            case 'buffet.csv':
                pass


