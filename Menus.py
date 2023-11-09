import datetime
class menuCliente():
    def __init__(self) -> None:
        pass
    def bienvenida(self, inputemail):
        
        print("-------------------------------------------------------------------------")
        print("Bienvenido al hotel")
        print("-------------------------------------------------------------------------")
        print ("1. Ver habitaciónes")
        print ("2. Ver mis reservas")
        print ("3. Ver Menú del Buffet")
        print ("4. Salir")
        
        opcion_menu = input("Ingrese una opción: ")
        from Index import instance
        if opcion_menu == "1":
           
            instance.roomManager.mostrar_habitaciones()
            print("-------------------------------------------------------------------------")
            inputconsulta=input('Quiere realizar una reserva? (s/n): ')
            if inputconsulta=='s':
                inputanoinicio=int(input('Ingrese el año de inicio de su estadia: '))
                inputmesinicio=int(input('Ingrese el mes de inicio de su estadia: '))
                inputdiainicio=int(input('Ingrese el dia de inicio de su estadia: '))
                inputanofin=int(input('Ingrese el año de fin de su estadia: '))
                inputmesfin=int(input('Ingrese el mes de fin de su estadia: '))
                inputdiafin=int(input('Ingrese el dia de fin de su estadia: '))
                inputtipo=input('Ingrese el tipo de habitacion que desea: ')
                inputbano=input('Ingrese si desea baño privado (s/n): ')
                inputbalcon=input('Ingrese si desea balcon (s/n): ')
                fecha_inicio=datetime.datetime(inputanoinicio,inputmesinicio,inputdiainicio,15,0)
                fecha_fin=datetime.datetime(inputanofin,inputmesfin,inputdiafin,10,0)
                
                print("-------------------------------------------------------------------------")
                instance.reservaManager.reservar(inputemail,fecha_inicio,fecha_fin,inputtipo,inputbano,inputbalcon)
            print("-------------------------------------------------------------------------")  
        elif opcion_menu == "2":
            print("-------------------------------------------------------------------------")
            print("Mis reservas")
            print("-------------------------------------------------------------------------")
            instance.reservaManager.mostrar_reservas(inputemail)
            inputcancelar=input('Desea cancelar alguna reserva? (s/n): ')
            if inputcancelar=='s':
                inputnroreserva=input('Ingrese el numero de reserva que desea cancelar: ')
                instance.reservaManager.cancelar_reserva(inputnroreserva)
            print("-------------------------------------------------------------------------")
        elif opcion_menu == "3":
            print("-------------------------------------------------------------------------")
            print("Menú del Buffet")
            print("-------------------------------------------------------------------------")  
            instance.buffet.mostrar_menu()
            inputpedir=input('Desea realizar algun pedido? (s/n): ')
            if inputpedir=='s':
                inputalimento=input('Ingrese el alimento que desea pedir: ')
                inputcant=int(input('Ingrese la cantidad que desea pedir: '))
                instance.buffet.tomar_pedido(inputemail,inputalimento,inputcant)
            else:
                inputver=input('Desea ver sus pedidos? (s/n): ')
                if inputver=='s':
                    instance.buffet.mostrar_pedido(inputemail)
            print("-------------------------------------------------------------------------")
        
        elif opcion_menu == "4":
            
            print("-------------------------------------------------------------------------")
            #aqui termina el programa
            return
        
class menuPersonal:
        def __init__(self) -> None:
            pass
        def inicio(self, inputemail):
             pass
class menuAdministrador:
        def __init__(self) -> None:
            pass
        def inicio(self, inputemail):
            print("-------------------------------------------------------------------------")
            print("Bienvenido al hotel")
            print("-------------------------------------------------------------------------")
            print ("1. Dar de baja personal")
            print ("2. Recibir informe")
            print ("3. Asignar tareas")
            print ("4. Salir")
            opcion_menu = input("Ingrese una opción: ")
            from Index import instance
            if opcion_menu=='1':
                instance.personalManager.mostrar_personal()
                inputbaja=input('Ingrese el email del personal que desea dar de baja: ')
                if inputbaja in instance.personalManager.lista_empleado:
                    instance.personalManager.dar_de_baja(inputbaja) 
                    print( 'El empleado ha sido dado de baja')
                else :
                    print('El email ingresado no corresponde a ningun empleado')
                print("-------------------------------------------------------------------------")   
            if opcion_menu=='2':
                pass
            if opcion_menu=='3':
               pass
            elif opcion_menu == "4":
                print("-------------------------------------------------------------------------")
                #aqui termina el programa
                return
        



    