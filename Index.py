from managers import * 
from discoDuro import DiscoDuro
from buffet import Buffet
from Menus import menuCliente, menuPersonal, menuAdministrador
from foto import *
class Hotel:
    def __init__(self):
        self.clienteManager=clienteManager()
        self.personalManager=personalManager()
        self.adminManager=adminManager()
        self.roomManager=roomManager()
        self.reservaManager=reservaManager()
        self.discoHotel1 = DiscoDuro()
        self.buffet = Buffet()
        self.menuCliente = menuCliente()
        self.menuPersonal = menuPersonal()
        self.menuAdministrador = menuAdministrador()

        
    def setup(self):

        listacsv=['users.csv', 'reservas.csv', 'room.csv','buffet.csv', 'tareas.csv', 'pedidos.csv','ingresos.csv','inversion.csv']
        for carpeta in listacsv:
            self.discoHotel1.leerSETUP(carpeta)
    def run(self):
        # Imprime Hotel 4.0
        print_image(image_path)
        print("--------------------------------------------------------------------------")
        start = "s"
        while start == "s":
            print("|Bienvenido a Hotel 4.0 - El hotel del futuro|")
            print("1. Registrarse")
            print("2. Iniciar sesión")
            print("3. Salir")
            
            opcion = input("Ingrese una opción: ")
            
            if opcion == "1":
                inputtypeuser = input("Ingrese el tipo de usuario ('cliente' o 'personal' + clave de personal): ")
                inputnombre = input("Ingrese su nombre: ")
                inputapellido = input("Ingrese su apellido: ")
                inputemail = input("Ingrese su email: ")
                inputpassword = input("Ingrese su contraseña: ")
                
                if inputtypeuser == "admin 1234":
                    self.adminManager.createAdmin(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword)
                elif inputtypeuser == "cliente": 
                    self.clienteManager.createCliente(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword)
                elif inputtypeuser == "personal 1234":
                    inputcargo=input("Ingrese su cargo: ")
                    
                    self.personalManager.createPersonal(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword,inputcargo,'')
                
                

                print(self.clienteManager.lista_cliente)
                print(self.personalManager.lista_empleado)
                print(self.adminManager.totalAdmins)
               
            elif opcion == "2":
                inputemail = input("Ingrese su email: ")
                inputpassword = input("Ingrese su contraseña: ")
                
                flag,typeUser = self.clienteManager.verificacion(inputemail,inputpassword)
                if flag == False:
                    flag,typeUser = self.personalManager.verificacion(inputemail,inputpassword)
                if flag == False:
                    flag,typeUser = self.adminManager.verificacion(inputemail,inputpassword)    
                if flag == True:
                    match typeUser: 
                        case "cliente": 
                                while True:
                                    self.menuCliente.bienvenida(inputemail)
                                    if input("¿Desea cerrar sesion? (s/n): ") == "s":
                                        break
                        case "personal 1234":
                            while True:
                                self.menuPersonal.bienvenida(inputemail)
                                if input("¿Desea cerrar sesion? (s/n): ") == "s":
                                    break
                        case "admin 1234":
                            while True:
                                self.menuAdministrador.inicio(inputemail)
                                if input("¿Desea cerrar sesion? (s/n): ") == "s":
                                    break
                                                
                else:
                    print("Usuario o contraseña incorrectos")
                    print("-------------------------------------------------------------------------")
                                
            elif opcion == "3":
                print("Gracias por utilizar nuestros servicios")
                break
instance = Hotel()           

