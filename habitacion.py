class Habitacion:
    def __init__(self,nro_habitacion,tipo,capacidad,precio,bano,balcon):
        self.nro_habitacion=nro_habitacion
        self.tipo=tipo
        self.capacidad=capacidad
        self.precio=precio
        self.bano=bano
        self.balcon=balcon
        self.ocupacion=False
    def ocuparhabitacion(self):
        if self.ocupacion==False:
            self.ocupacion == True
    
    def liberarhabitacion(self):
        self.ocupacion = False
            
            
class Nodo:
    def __init__(self, habitacion):
        self.habitacion = habitacion
        self.prox = None