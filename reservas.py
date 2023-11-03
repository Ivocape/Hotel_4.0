class Reserva:
    def __init__ (self, cliente, fecha_inicio, fecha_fin, tipo_habit,balcon,bano):
        self.cliente=cliente
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.balcon=balcon
        self.bano=bano
        self.nro_reserva= cliente.dni+fecha_inicio