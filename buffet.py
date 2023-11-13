import datetime

class Buffet:
    def __init__ (self):
        self.menu={}
        self.lista_pedidos=[]
    def cache(self, alimento, precio, cant): #Lee el archivo buffet.csv y lo guarda en el diccionario menu
        self.menu[alimento]=("$"+ precio,int(cant)) #esto tambien es una tupla

        #self.menu[alimento] = ("$"+ precio,cant -1)
    def cache_pedidos(self, cliente, alimento, cant_pedida, total, fecha): #Lee el archivo pedidos.csv y lo guarda en la lista lista_pedidos
        self.lista_pedidos.append([cliente,alimento,cant_pedida,total,fecha])
        
    def agregar_menu (self, alimento, precio): #Agrega un alimento al menu
        alimento=alimento.lower()
        self.menu [alimento]=("$"+ str(precio),0) 
        from Index import instance
        instance.discoHotel1.escribir(carpeta='buffet.csv',alimento=alimento,precio=precio,cant=0)
        print('Alimento agregado al menú')
    def reponer_cant (self, alimento, agregado): #Reabastece la cantidad de un alimento
        alimento=alimento.lower()
        if alimento in self.menu:
            for alimento, (precio, cant) in self.menu.items():
                nuevacant=cant+agregado
                self.menu[alimento]=(self.menu[alimento][0],nuevacant)
                from Index import instance
                instance.discoHotel1.reponer_cant(alimento,nuevacant)
                print(f'Cantidad de {alimento} reabastecida')
        else:
            print(f"El pedido {alimento} no se encuentra en el menú")

    def modificar_precio (self, alimento, precio): #Modifica el precio de un alimento
        alimento=alimento.lower()
        if alimento in self.menu:
            self.menu[alimento]=("$"+str(precio),self.menu[alimento][1])
            from Index import instance
            instance.discoHotel1.cambiar_precio_comida(alimento,precio)
            print(f'Precio de {alimento} modificado')
        else:
            print(f"El pedido {alimento} no se encuentra en el menú")

    def eliminar_alimento (self, alimento): #Elimina un alimento del menu
        alimento=alimento.lower()
        if alimento in self.menu:
            del self.menu[alimento]
            from Index import instance
            instance.discoHotel1.eliminar_alimento(alimento)
            print('Alimento eliminado del menú')
        else:
            print(f"El {alimento} no se encuentra disponible")

    def mostrar_menu(self): #Muestra el menu
        print('Alimento -  Precio')
        for alimento, (precio, cant) in self.menu.items():
            
            print(f"{alimento} -  {precio}")

    def tomar_pedido(self, cliente, alimento, cant_pedida): #Toma un pedido
        alimento=alimento.lower()
        if alimento in self.menu:
            if self.menu[alimento][1]>=cant_pedida:
                    self.menu[alimento]=[self.menu[alimento][0],self.menu[alimento][1]-cant_pedida]
                    precio_unitario = int(self.menu[alimento][0].replace("$",""))
                    total=precio_unitario*cant_pedida
                    self.lista_pedidos.append([cliente,alimento,cant_pedida,total,datetime.datetime.now()])
                    from Index import instance
                    instance.discoHotel1.escribir(carpeta='pedidos.csv',cliente=cliente,alimento=alimento,cant_pedida=cant_pedida,total=total,fecha=datetime.datetime.now())
                    print(f'{cant_pedida} de {alimento} solicitada con exito')
                    return total
            elif self.menu[alimento][1]<cant_pedida and self.menu[alimento][1]>0: 
                    precio_unitario = int(self.menu[alimento][0].replace("$",""))
                    total=precio_unitario*self.menu[alimento][1]
                    self.lista_pedidos.append([cliente,alimento,self.menu[alimento][1],datetime.datetime.now()])
                    print(f'{self.menu[alimento][1]} de {alimento} solicitada con exito')
                    from Index import instance
                    instance.discoHotel1.escribir(carpeta='pedidos.csv',cliente=cliente,alimento=alimento,cant_pedida=self.menu[alimento][1],total=total,fecha=datetime.datetime.now())
                    self.menu[alimento]=[self.menu[alimento][0],0]
                    return total
                    
            else:
              print("El alimento no está disponible")
                
        else:
            print("El alimento no existe")

    def mostrar_pedido(self, cliente): #Muestra los pedidos de un cliente
        pedidos_cliente = [pedido for pedido in self.lista_pedidos if pedido[0] == cliente]
        if pedidos_cliente:
            print(f"Pedidos de {cliente}:")
            for pedido in pedidos_cliente:
                cliente, alimento, cant_pedida, total, timestamp = pedido
                print(f"Alimento: {alimento}, Cantidad Pedida: {cant_pedida}, precio {total}, fecha de compra {timestamp}")
        else:
            print(f"No se encontraron pedidos para {cliente}.")
            