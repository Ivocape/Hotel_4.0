class Reserva:
    def __init__ (self, mail, fecha_inicio, fecha_fin, tipo_habit,balcon,bano):
        self.mail=mail
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.balcon=balcon
        self.bano=bano
        self.tipo_habit=tipo_habit
        self.nro_reserva= mail+str(fecha_inicio.date())
        self.nro_habitacion=0
        self.total=0