from managers import * 
from discoDuro import DiscoDuro
from buffet import Buffet
class Hotel:
    def __init__(self):
        self.clienteManager=clienteManager()
        self.personalManager=personalManager()
        self.adminManager=adminManager()
        self.roomManager=roomManager()
        self.reservaManager=reservaManager()
        self.discoHotel1 = DiscoDuro()
        self.buffet = Buffet()
        #self.personalManager.createPersonal("personal 1234","Juan","Perez", "AAA","1234")
    def setup(self):

        listacsv=['users.csv', 'reservas.csv', 'room.csv','buffet.csv']
        for carpeta in listacsv:
            self.discoHotel1.leerSETUP(carpeta)
    def run(self):
        #self.personalManager.createPersonal("personal 1234","Juan","Perez", "AAA","1234")
        print("Bienvenido al hotel")
        start = input("¿Desea iniciar sesión? (s/n): ")
        while start == "s":
            print("1. Registrarse")
            print("2. Iniciar sesión")
            print("3. Modificar datos")
            print("4. Salir")
            
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
                    self.personalManager.createPersonal(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword)
                
                print("Usuario creado con éxito, por favor inicie sesión")

                print(self.clienteManager.lista_cliente)
                print(self.personalManager.lista_empleado)
                print(self.adminManager.totalAdmins)
               
            elif opcion == "2":
                inputemail = input("Ingrese su email: ")
                inputpassword = input("Ingrese su contraseña: ")
               
                print(self.clienteManager.verificacion(inputemail,inputpassword))
                if   self.clienteManager.verificacion(inputemail,inputpassword) == True:
                    print("-------------------------------------------------------------------------")
                    print("Bienvenido al hotel")
                    print("-------------------------------------------------------------------------")
                    print ("1. Reservar habitación")
                    print ("2. Ver mis reservas")
                    print ("3. Ver Menú del Buffet")
                    print ("4. Salir")
                    
                    opcion_menu = input("Ingrese una opción: ")
            
                    if opcion_menu == "1":
                        print("-------------------------------------------------------------------------")
                        print("Habitaciones disponibles")
                        print("-------------------------------------------------------------------------")
                        self.roomManager.mostrar_habitaciones()
                        print("-------------------------------------------------------------------------")
                        print("Tipos de habitaciones")
                        print("-------------------------------------------------------------------------")
                        self.roomManager.mostrar_tipos_habitaciones()
                        print("-------------------------------------------------------------------------")
                        print("Servicios")
                        print("-------------------------------------------------------------------------")
                        self.roomManager.mostrar_servicios()
                        print("-------------------------------------------------------------------------")
                        print("Precios")
                        print("-------------------------------------------------------------------------")
                        self.roomManager.mostrar_precios()
                        print("-------------------------------------------------------------------------")
                        print("Reservar habitación")
                        print("-------------------------------------------------------------------------")
                        inputtipo = input("Ingrese el tipo de habitación: ")
                        inputnumero = input("Ingrese el número de habitación: ")
                        inputfecha = input("Ingrese la fecha de reserva: ")
                        inputdias = input("Ingrese la cantidad de días: ")
                        inputservicios = input("Ingrese los servicios: ")
                        self.reservaManager.createReserva(inputemail,inputtipo,inputnumero,inputfecha,inputdias,inputservicios)
                        print("-------------------------------------------------------------------------")
                        print("Reserva realizada con éxito")
                        print("-------------------------------------------------------------------------")
                    elif opcion_menu == "2":
                        print("-------------------------------------------------------------------------")
                        print("Mis reservas")
                        print("-------------------------------------------------------------------------")
                        self.reservaManager.mostrar_reservas(inputemail)
                        print("-------------------------------------------------------------------------")
                    elif opcion_menu == "3":
                        print("-------------------------------------------------------------------------")
                        print("Menú del Buffet")
                        print("-------------------------------------------------------------------------")  
                        self.buffet.mostrar_menu()
                    elif opcion_menu == "4":
                            print("Gracias por utilizar nuestros servicios")
                            break         
                else:
                    print("Usuario o contraseña incorrectos")
                    print("-------------------------------------------------------------------------")
                                
                

            elif opcion == "3":
                # inputnombre = input("Ingrese su nombre: ")
                # inputpassword = input("Ingrese su contraseña: ")
                # self.userManager.modifyUser(inputnombre,inputpassword)
                print("-------------------------------------------------------------------------")
           
            elif opcion == "4":
                print("Gracias por utilizar nuestros servicios")
                break
instance = Hotel()           


instance.setup()
instance.run()
            
        
        

