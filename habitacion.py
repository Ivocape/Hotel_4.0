class Habitacion:
    def __init__(self,tipo,capacidad,precio,bano,balcon):
        self.tipo=tipo
        self.capacidad=capacidad
        self.precio=precio
        self.bano=bano
        self.balcon=balcon
        self.ocupacion=False
    def ocuparhabitacion(self):
        if self.ocupacion==False:
            self.ocupacion == True