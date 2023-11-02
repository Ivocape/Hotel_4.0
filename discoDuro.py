import csv
#####################################################################################
# ESTE DISCO DURO DEBE DE ENCARGARSE DE GUARDAR TODA INFORMACION DE USUARIOS, CLIENTES, PERSONAL, ADMINS,
#
#####################################################################################
class DiscoDuro():
    # Create a list to store the user information
    def __init__(self) -> None:
        self.users = []

    def leer (self, carpeta):    
        # Open the CSV file
        with open(carpeta, newline='') as csvfile: 
            # Create a CSV reader object
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            
            match carpeta:
#'users.csv', 'reservas.csv', 'room.csv','buffet.csv' BORRAR ESTO #####
                case "users.csv":
                     # Loop through each row in the CSV file
                    for row in reader:
                     # Extract the user information from the row
                        name = row[0]
                        surname = row[1]
                        email = row[2]
                        password = row[3]
                    # Add the user information to the list
                        self.users.append({'name': name, 'surname': surname, 'email': email , 'password': password})
                     # Print the user information
                    for user in self.users:
                     print(user['name'], user['surname'], user['email'], user['password'])
                    pass
                case 'reservas.csv':
                    for row in reader:
                        #falta dustin

                    pass
                case 'room.csv':
                    pass

       


    def escribir (self,name, surname, email, password):
        # Open the CSV file in append mode
        with open('users.csv', 'a', newline='') as csvfile:
            # Create a CSV writer object
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            # Write the user information to the CSV file
            writer.writerow([name, surname, email, password])
            self.users.append({'name': name, 'surname': surname, 'email': email , 'password': password})

discoHotel1 = DiscoDuro()
