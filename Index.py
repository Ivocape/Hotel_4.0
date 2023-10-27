from managers import * 

class Hotel:
    def __init__(self):
        self.clienteManager=clienteManager()
        self.personalManager=personalManager()
        self.adminManager=adminManager()
        self.roomManager=roomManager()
        self.reservaManager=reservaManager()
        self.userManager=userManager()
        

    def run(self):
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
                    adminManager.createAdmin(inputnombre,inputapellido,inputemail,inputpassword)
                elif inputtypeuser == "cliente": 
                    userManager.createUser(inputnombre,inputapellido,inputemail,inputpassword)
                elif inputtypeuser == "personal 1234":
                    personalManager.createPersonal(inputnombre,inputapellido,inputemail,inputpassword)
                opcion = 2
                print("Usuario creado con éxito, por favor inicie sesión")
                print("-------------------------------------------------------------------------")
            elif opcion == "2":
                inputemail = input("Ingrese su email: ")
                inputpassword = input("Ingrese su contraseña: ")
                
                userManager.validateUser(inputemail,inputpassword)
                if True: 
                    pass
                    
            

if __name__ == "__main__":
    instance=Hotel()
    
    instance.run()
        
        
        

