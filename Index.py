
from managers import * 
from discoDuro import DiscoDuro
class Hotel:
    def __init__(self):
        self.clienteManager=clienteManager()
        self.personalManager=personalManager()
        self.adminManager=adminManager()
        self.roomManager=roomManager()
        self.reservaManager=reservaManager()
        self.userManager=userManager()
        self.discoHotel1 = DiscoDuro()

        #self.personalManager.createPersonal("personal 1234","Juan","Perez", "AAA","1234")
    def setup(self):
        self.discoHotel1.leerSETUP()
        pass
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
                print(self.userManager)
                if inputtypeuser == "admin 1234":
                    self.adminManager.createAdmin(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword)
                elif inputtypeuser == "cliente": 
                    self.clienteManager.createCliente(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword)
                    print(self.userManager)
                elif inputtypeuser == "personal 1234":
                    self.personalManager.createPersonal(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword)
                
                print("Usuario creado con éxito, por favor inicie sesión")
                print(self.clienteManager.lista_cliente)
                print(self.personalManager.lista_empleado)
                print(self.adminManager.totalAdmins)

                print("-------------------------------------------------------------------------")
            elif opcion == "2":
                inputemail = input("Ingrese su email: ")
                inputpassword = input("Ingrese su contraseña: ")
                
               
                if  self.userManager.validateUser(inputemail,inputpassword): 
                    print("Bienvenido")
                    print("-------------------------------------------------------------------------")
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

if __name__ == "__main__":
    instance.setup()
    instance.run()
        
        
        

