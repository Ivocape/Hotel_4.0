import csv
#####################################################################################
# ESTE DISCO DURO DEBE DE ENCARGARSE DE GUARDAR TODA INFORMACION DE USUARIOS, CLIENTES, PERSONAL, ADMINS,
#z
#####################################################################################
class DiscoDuro():
    # Create a list to store the user information
    def __init__(self) -> None:
        pass

    def leer (self, carpeta):    

        # Open the CSV file
        with open(carpeta, newline='') as csvfile: 
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
                     # Add the user information to the list
                    from Index import instance #Aca importamos la instancia de la clase Hotel
                    instance.userManager.createUser(row[4], name, surname, email, password)
                    if inputtypeuser == "admin 1234":
                        instance.adminManager.createAdmin(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword)
                    elif inputtypeuser == "cliente": 
                        instance.clienteManager.createCliente(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword)
                    elif inputtypeuser == "personal 1234":
                        instance.personalManager.createPersonal(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword)
                    # Print the user information
                    for user in self.users:
                        print(user['name'], user['surname'], user['email'], user['password'])
                case 'reservas.csv':
                    pass
                case 'room.csv':
                    pass
                case 'buffet.csv':
                      pass


    def escribir (self, carpeta, **kwargs):
        from Index import instance #Aca importamos la instancia de la clase Hotel
        match carpeta:
            case 'users.csv':
                # Open the CSV file in append mode
                instance.userManager.createUser(kwargs["typeUser"],kwargs['name'], kwargs['surname'], kwargs['email'],kwargs['password'])
                
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

discoHotel1 = DiscoDuro()

