import datetime
class Buffet:
    def __init__ (self):
        self.menu={"Desayuno básico": ["$1000", 20], "Desayuno premium":["$2000", 15], "Bebida":["$200", 40], "Medialunas":["$450", 36], "Sandwich":["$600", 20],
                    "Tostadas":["$500", 35], "Cena":["$2000", 25], "Cena premium":["$3500", 15]}
        self.lista_pedidos=[]

    def agregar_menu (self, alimento, precio):
        self.menu [alimento]=("$"+ precio,0) 

    def reponer_cant (self, alimento, cant):
        if alimento in self.menu:
            self.menu[alimento]=(self.menu[alimento][0],cant)
        else:
            print("El pedido " + {alimento} + " no se encuentra en el menú")

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
                    self.lista_pedidos.append([cliente,alimento,cant_pedida,precio_unitario*cant_pedida,datetime.datetime.now()])
            elif self.menu[alimento][1]<cant_pedida and self.menu[alimento][1]>0: 
                    precio_unitario = int(self.menu[alimento][0].replace("$",""))
                    self.lista_pedidos.append([cliente,alimento,self.menu[alimento][1],precio_unitario*self.menu[alimento][1],datetime.datetime.now()])
                    self.menu[alimento]=[self.menu[alimento][0],0]
                    
                    
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
            