class menuCliente():
    def __init__(self) -> None:
        pass
    def run():
        #menu del cliente para generar reservas y ver sus datos

        print("Bienvenido al menu de cliente")
        print("1. Generar reserva")
        print("2. Ver mis datos")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            print("Indique la fecha de ingreso y egreso")
            fecha_ingreso = input("Ingrese la fecha de ingreso: ")
            fecha_egreso = input("Ingrese la fecha de egreso: ")
            print("Indique la cantidad de personas")
            cantidad_personas = input("Ingrese la cantidad de personas: ")
            print("Indique el tipo de habitacion")
            tipo_habitacion = input("Ingrese el tipo de habitacion: ")

            from Index import instance
            instance.reservaManager.agregar_reserva()
            
            print("-------------------------------------------------------------------------")
        elif opcion == "2":
            print("Ver mis datos")
            print("-------------------------------------------------------------------------")
        elif opcion == "3":
            print("Gracias por utilizar nuestros servicios")
            print("-------------------------------------------------------------------------")
            return False