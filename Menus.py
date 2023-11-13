import datetime
class menuCliente():
    def __init__(self) -> None:
        pass
    def bienvenida(self, inputemail):
        
        print("-------------------------------------------------------------------------")
        print(f"Bienvenido al hotel del futuro {inputemail}! Usted a accedido como cliente y estas son sus opciones:")
        print("-------------------------------------------------------------------------")
        print ("1. Ver habitaciónes") #cliente ve las habitaciones disponibles
        print ("2. Ver mis reservas") #cliente ve sus reservas
        print ("3. Ver Menú del Buffet") #cliente ve el menu del buffet
        
        print ("4. Salir")
        
        opcion_menu = input("Ingrese una opción: ")
        from Index import instance
        if opcion_menu == "1":
           
            instance.roomManager.mostrar_habitaciones()
            print("-------------------------------------------------------------------------")
            inputconsulta=input('Quiere realizar una reserva? (s/n): ')
            if inputconsulta=='s':
                inputanoinicio=(input('Ingrese el año de inicio de su estadia: '))
                inputmesinicio=(input('Ingrese el mes de inicio de su estadia: '))
                inputdiainicio=(input('Ingrese el dia de inicio de su estadia: '))
                inputanofin=(input('Ingrese el año de fin de su estadia: '))
                inputmesfin=(input('Ingrese el mes de fin de su estadia: '))
                inputdiafin=(input('Ingrese el dia de fin de su estadia: '))
                if inputanoinicio.isdigit() and inputmesinicio.isdigit() and inputdiainicio.isdigit() and inputanofin.isdigit() and inputmesfin.isdigit() and inputdiafin.isdigit():
                    inputanoinicio=int(inputanoinicio)
                    inputmesinicio=int(inputmesinicio)
                    inputdiainicio=int(inputdiainicio)
                    inputanofin=int(inputanofin)
                    inputmesfin=int(inputmesfin)
                    inputdiafin=int(inputdiafin)
                else:
                    print('Ingrese una fecha valida TODO EN NUMEROS')
                    return
                inputtipo=input('Ingrese el tipo de habitacion que desea: ')
                inputbano=input('Ingrese si desea baño privado (s/n): ')
                inputbalcon=input('Ingrese si desea balcon (s/n): ')
                fecha_inicio=datetime.datetime(inputanoinicio,inputmesinicio,inputdiainicio,15,0)
                fecha_fin=datetime.datetime(inputanofin,inputmesfin,inputdiafin,10,0)
                
                print("-------------------------------------------------------------------------")
                instance.clienteManager.reservar(inputemail,fecha_inicio,fecha_fin,inputtipo,inputbano,inputbalcon)
            print("-------------------------------------------------------------------------")  
        elif opcion_menu == "2":
            print("-------------------------------------------------------------------------")
            print("Mis reservas")
            print("-------------------------------------------------------------------------")
            instance.reservaManager.mostrar_reservas(inputemail)
            inputcancelar=input('Desea cancelar alguna reserva? (s/n): ')
            if inputcancelar=='s':
                inputnroreserva=input('Ingrese el numero de reserva que desea cancelar: ')
                instance.reservaManager.cancelar_reserva(inputemail,inputnroreserva)
            print("-------------------------------------------------------------------------")
        elif opcion_menu == "3":
            print("-------------------------------------------------------------------------")
            print("Menú del Buffet")
            print("-------------------------------------------------------------------------")  
            instance.buffet.mostrar_menu()
            inputpedir=input('Desea realizar algun pedido? (s/n): ')
            if inputpedir=='s':
                inputalimento=input('Ingrese el alimento que desea pedir: ')
                inputcant=input('Ingrese la cantidad que desea pedir: ')
                if inputcant.isdigit():
                    inputcant=int(inputcant)
                else:
                    print('Ingrese una cantidad valida, USANDO SOLO NUMEROS')
                    return
                instance.clienteManager.pedir_comida(inputemail,inputalimento,inputcant)
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
        def bienvenida(self, inputemail):
            print("-------------------------------------------------------------------------")
            print(f"Hola {inputemail}! Has accedido como personal del hotel y estas son sus opciones:")
            print("-------------------------------------------------------------------------")
            print ("1. Registrar Ingreso") #empleado ingresa en el dia a trabajar en el hotel
            print ("2. Tomar tarea") #empleado toma una tarea para realizar
            print ("3. Reponer cantidad en el buffet")#empleado repone la cantidad de un alimento en el buffet
            print('4. Completar tarea') #empleado completa una tarea que tenia asignada     
            print ("5. Registrar Egreso") #empleado egresa del hotel
            print ("6. Salir") #empleado cierra sesion 
            
            opcion_menu = input("Ingrese una opción: ")
            from Index import instance
            if opcion_menu == "1":
                instance.personalManager.registrar_ingreso(inputemail)
                print ("Bienvenido. Se registró su ingreso al hotel")
                print("-------------------------------------------------------------------------")
            elif opcion_menu == "2":
                instance.personalManager.asignacion_tareas(inputemail)
                print("-------------------------------------------------------------------------")
            elif opcion_menu == "3":
                instance.buffet.mostrar_menu()
                inputalimento=input('Ingrese el alimento que desea reponer: ')
                inputcant=input('Ingrese la cantidad que desea reponer: ')
                if inputcant.isdigit():
                    inputcant=int(inputcant)
                else:
                    print('Ingrese una cantidad valida, USANDO SOLO NUMEROS')
                    return

                instance.buffet.reponer_cant(inputalimento,inputcant)
                print("-------------------------------------------------------------------------")
            elif opcion_menu == "4":
                instance.personalManager.completar_tarea(inputemail)
                print("-------------------------------------------------------------------------")
            elif opcion_menu == "5":
                instance.personalManager.registrar_egreso(inputemail)
                print ("Hasta luego. Se registró su egreso del hotel")
                print("-------------------------------------------------------------------------")
            elif opcion_menu == "6":
                print("-------------------------------------------------------------------------")
                #aqui termina el programa
                return

               
                
class menuAdministrador:
        def __init__(self) -> None:
            pass
        def inicio(self, inputemail):
            print("-------------------------------------------------------------------------")
            print(f"Buenos dias Jefe {inputemail}! En que puedo servirte? Estas son sus opciones:")
            print("-------------------------------------------------------------------------")
            print ("1. Dar de baja personal") #admin da de baja a un empleado
            print ("2. Recibir informes ") #admin ve los informes de ocupacion, recaudacion y categorizacion de clientes
            print ("3. Asignar tareas a todos los empleados libres") #admin asigna tareas a todos los empleados libres
            print('4. Crear tarea') #admin crea una tarea
            print ('5. Modificar el buffet') #admin modifica el menu del buffet
            print ('6. Ver ingresos y egresos del personal') #admin ve los ingresos y egresos del personal
            
            print ("7. Salir")
            print("-------------------------------------------------------------------------")
            opcion_menu = input("Ingrese una opción: ")
            print("-------------------------------------------------------------------------")
            from Index import instance
            if opcion_menu=='1':
                instance.personalManager.mostrar_personal()
                inputbaja=input('Ingrese el email del personal que desea dar de baja: ')
                instance.personalManager.dar_de_baja(inputbaja) 
                print("-------------------------------------------------------------------------")   
            elif opcion_menu=='2':
                
                print('1. Informe de ocupacion del hotel')
                print('2. Informe de recaudacion del hotel')
                print('3. Informe de categorizacion de clientes')
                print("-------------------------------------------------------------------------")
                opcion_informe=input('Ingrese el informe que desea recibir: ')
                if opcion_informe=='1':
                    instance.adminManager.mostrar_informe()
                elif opcion_informe=='2':
                    inputano=(input('Ingrese el año de busqueda: '))
                    inputmes=(input('Ingrese el mes de busqueda: '))
                    inputdia=(input('Ingrese el dia de busqueda: '))
                    if inputano.isdigit() and inputmes.isdigit() and inputdia.isdigit():
                        inputano=int(inputano)
                        inputmes=int(inputmes)
                        inputdia=int(inputdia)
                    else:
                        print('Ingrese una fecha valida TODO EN NUMEROS')
                        return
                    inputfecha=datetime.datetime(inputano,inputmes,inputdia)
                    instance.adminManager.informe_recaudacion_diaria(inputfecha)
                elif opcion_informe=='3':
                    inputprimervalor=input('Ingrese el primer valor de la categoria: ')
                    inputsegundovalor=input('Ingrese el segundo valor de la categoria: ')
                    if inputprimervalor.isdigit() and inputsegundovalor.isdigit():
                        inputprimervalor=int(inputprimervalor)
                        inputsegundovalor=int(inputsegundovalor)
                    else:
                        print('Ingrese un valor valido TODO EN NUMEROS')
                        return
                    instance.adminManager.categorizar_cliente(inputprimervalor,inputsegundovalor)
                print("-------------------------------------------------------------------------")
            elif opcion_menu=='3':
                
                instance.personalManager.asignacion_tareas_todos()
                print("-------------------------------------------------------------------------")
                print('Se asignaron las tareas a los empleados libres y las restantes son: ')
                instance.personalManager.mostrar_tareas()
                print("-------------------------------------------------------------------------")
            elif opcion_menu=='4':
                inputtarea=input('Ingrese la tarea que desea agregar: ')
                inputcargo=input('Ingrese el cargo al que pertenece la tarea: ')
                instance.personalManager.nuevatarea(inputtarea,inputcargo)
                print("-------------------------------------------------------------------------")
            elif opcion_menu=='5':
                instance.buffet.mostrar_menu()
                inputagregar=input('Desea agregar alguna opcion al menu? (s/n): ')
                if inputagregar=='s':
                    inputalimento=input('Ingrese el alimento que desea agregar: ')
                    inputprecio=input('Ingrese el precio del alimento en numeros sin $: ')
                    if inputprecio.isdigit():
                        inputprecio=int(inputprecio)
                    else:
                        print('Ingrese un precio valido, USANDO SOLO NUMEROS')
                        return
                    instance.buffet.agregar_menu(inputalimento,inputprecio)
                else:
                    inputeliminar=input('Desea eliminar alguna opcion del menu? (s/n): ')
                    if inputeliminar=='s':
                        inputalimento=input('Ingrese el alimento que desea eliminar: ')
                        instance.buffet.eliminar_alimento(inputalimento)
                    else:
                        inputeliminar=input('Desea modificar el precio de alguna opcion del menu? (s/n): ')
                        if inputeliminar=='s':
                            inputalimento=input('Ingrese el alimento que desea modificar: ')
                            inputprecio=input('Ingrese el nuevo precio del alimento en numeros sin $: ')
                            if inputprecio.isdigit():
                                inputprecio=int(inputprecio)
                            else:
                                print('Ingrese un precio valido, USANDO SOLO NUMEROS')
                                return
                            instance.buffet.modificar_precio(inputalimento,inputprecio)
                print("-------------------------------------------------------------------------")
            elif opcion_menu=='6':
                instance.personalManager.mostrar_ingresos()
                print("-------------------------------------------------------------------------")
            elif opcion_menu == "7":
                print("-------------------------------------------------------------------------")
                #aqui termina el programa
                return
        



    