import datetime

class Buffet:
    def __init__ (self):
        self.menu={}
        self.lista_pedidos=[]
    def cache(self, alimento, precio, cant):
        self.menu[alimento]=("$"+ precio,cant) #esto tambien es una tupla

        #self.menu[alimento] = ("$"+ precio,cant -1)
      
    def agregar_menu (self, alimento, precio):
        self.menu [alimento]=("$"+ precio,0) 

    def reponer_cant (self, alimento, cant):
        for alimento, (precio, cant) in self.menu.items():
            self.menu[alimento]=(self.menu[alimento][0],cant)
        else:
            print(f"El pedido {alimento} no se encuentra en el menú")

    def modificar_precio (self, alimento, precio):
        if alimento in self.menu:
            self.menu[alimento]=("$"+precio,self.menu[alimento][1])
        else:
            print("El pedido " + {alimento} + " no se encuentra en el menú")

    def eliminar_alimento (self, alimento):
        if alimento in self.menu:
            del self.menu[alimento]
        else:
            print("La orden " + {alimento} + " no se encuentra disponible")

    def mostrar_menu(self):
        print('Alimento -  Precio')
        for alimento, (precio, cant) in self.menu.items():
            
            print(f"{alimento} -  {precio}")

    def tomar_pedido(self, cliente, alimento, cant_pedida):
        if alimento in self.menu:
            if self.menu[alimento][1]>=cant_pedida:
                    self.menu[alimento]=[self.menu[alimento][0],self.menu[alimento][1]-cant_pedida]
                    precio_unitario = int(self.menu[alimento][0].replace("$",""))
                    total=precio_unitario*cant_pedida
                    self.lista_pedidos.append([cliente,alimento,cant_pedida,total,datetime.datetime.now()])
                    print(f'{cant_pedida} de {alimento} solicitada con exito')
                    return total
            elif self.menu[alimento][1]<cant_pedida and self.menu[alimento][1]>0: 
                    precio_unitario = int(self.menu[alimento][0].replace("$",""))
                    total=precio_unitario*self.menu[alimento][1]
                    self.lista_pedidos.append([cliente,alimento,self.menu[alimento][1],datetime.datetime.now()])
                    print(print(f'{self.menu[alimento][1]} de {alimento} solicitada con exito'))
                    self.menu[alimento]=[self.menu[alimento][0],0]
                    return total
                    
            else:
              print("El alimento no está disponible")
                
        else:
            print("El alimento no existe")

    def mostrar_pedido(self, cliente):
        pedidos_cliente = [pedido for pedido in self.lista_pedidos if pedido[0] == cliente]
        if pedidos_cliente:
            print(f"Pedidos de {cliente}:")
            for pedido in pedidos_cliente:
                cliente, alimento, cant_pedida, total, timestamp = pedido
                print(f"Alimento: {alimento}, Cantidad Pedida: {cant_pedida}, precio {total}, fecha de compra {timestamp}")
        else:
            print(f"No se encontraron pedidos para {cliente}.")
            