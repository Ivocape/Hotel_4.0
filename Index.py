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
                        inputanoinicio=input('Ingrese el año de inicio de su estadia')
                        inputmesinicio=input('Ingrese el mes de inicio de su estadia')
                        inputdiainicio=input('Ingrese el dia de inicio de su estadia')
                        inputanofin=input('Ingrese el año de fin de su estadia')
                        inputmesfin=input('Ingrese el mes de fin de su estadia')
                        inputdiafin=input('Ingrese el dia de fin de su estadia')
                        inputtipo=input('Ingrese el tipo de habitacion que desea')
                        inputbano=input('Ingrese si desea baño privado (s/n)')
                        inputbalcon=input('Ingrese si desea balcon (s/n)')
                        print("-------------------------------------------------------------------------")
                        self.clienteManager.reservar(inputemail,inputanoinicio,inputmesinicio,inputdiainicio,inputanofin,inputmesfin,inputdiafin,inputtipo,inputbano,inputbalcon)
                        print("-------------------------------------------------------------------------")  
                    elif opcion_menu == "2":
                        print("-------------------------------------------------------------------------")
                        print("Mis reservas")
                        print("-------------------------------------------------------------------------")
                        self.reservaManager.mostrar_reservas(inputemail)
                        inputcancelar=input('Desea cancelar alguna reserva? (s/n)')
                        if inputcancelar=='s':
                            inputnroreserva=input('Ingrese el numero de reserva que desea cancelar')
                            self.reservaManager.cancelar_reserva(inputnroreserva)
                        print("-------------------------------------------------------------------------")
                    elif opcion_menu == "3":
                        print("-------------------------------------------------------------------------")
                        print("Menú del Buffet")
                        print("-------------------------------------------------------------------------")  
                        self.buffet.mostrar_menu()
                        inputpedir=input('Desea realizar algun pedido? (s/n)')
                        if inputpedir=='s':
                            inputalimento=input('Ingrese el alimento que desea pedir')
                            inputcant=int(input('Ingrese la cantidad que desea pedir'))
                            self.buffet.tomar_pedido(inputemail,inputalimento,inputcant)
                        else:
                            inputver=input('Desea ver sus pedidos? (s/n)')
                            if inputver=='s':
                                self.buffet.mostrar_pedido(inputemail)
                        print("-------------------------------------------------------------------------")
                    
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



        

