import datetime

class Hotel:
    def __init__(self):
        
        self.clienteManager=Cliente_Manager()
        
    def run(self):
        pass
    

if __name__ == "__main__":
    instance=Hotel()
    
    instance.run()
        
        
        

start = input("¿Desea iniciar sesión? (s/n): ")
while start == "s":
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Modificar datos")
    print("4. Salir")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        inputtypeuser = input("Ingrese el tipo de usuario: ")
        inputnombre = input("Ingrese su nombre: ")
        inputapellido = input("Ingrese su apellido: ")
        inputemail = input("Ingrese su email: ")
        inputpassword = input("Ingrese su contraseña: ")
        if inputtypeuser == "admin":
            adminManager.createUser(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword)
        elif   
            userManager.createUser(inputtypeuser,inputnombre,inputapellido,inputemail,inputpassword)

    elif opcion == "2":
        inputemail = input("Ingrese su email: ")
        inputpassword = input("Ingrese su contraseña: ")
        
        userManager.validateUser(inputemail,inputpassword)
        if True:
            

            
