class Reserva:
    def __init__ (self, nro_reserva, mail, fecha_inicio, fecha_fin, nro_habitacion,total,fecha_reserva):
        self.mail=mail
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.nro_reserva= nro_reserva
        self.nro_habitacion=nro_habitacion
        self.total=total
        self.fecha_reserva=fecha_reserva
        
        
class Nodo_recaudacion():
    def __init__(self, value):
        self.value=value
        self.prox=None