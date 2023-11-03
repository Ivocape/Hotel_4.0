import csv
#####################################################################################
# ESTE DISCO DURO DEBE DE ENCARGARSE DE GUARDAR TODA INFORMACION DE USUARIOS, CLIENTES, PERSONAL, ADMINS,
#
#####################################################################################
class DiscoDuro():
    # Create a list to store the user information
    def __init__(self) -> None:
        pass

    def leer (self):    
        # Open the CSV file
        with open('users.csv', newline='') as csvfile:
            # Create a CSV reader object
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            
            # Loop through each row in the CSV file
            for row in reader:
                # Extract the user information from the row
                
                name = row[0]
                surname = row[1]
                email = row[2]
                password = row[3]
                typeUser = row[4]
                # Add the user information to the list
                from Index import instance #Aca importamos la instancia de la clase Hotel
                if typeUser == "admin 1234":
                    instance.adminManager.createAdmin(typeUser,name,surname,email,password)
                elif typeUser == "cliente": 
                    instance.clienteManager.createCliente(typeUser,name,surname,email,password)
                elif typeUser == "personal 1234":
                    instance.personalManager.createPersonal(typeUser,name,surname,email,password)

        # Print the user information
        for user in instance.userManager.totalUsers:
            print(user.name, user.surname, user.email, user.password, user.typeUser)
       


    def escribir (self,typeUser,name, surname, email, password):
        # Open the CSV file in append mode
        with open('users.csv', 'a', newline='') as csvfile:
            # Create a CSV writer object
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            # Write the user information to the CSV file
            writer.writerow([name, surname, email, password,typeUser])

discoHotel1 = DiscoDuro()

