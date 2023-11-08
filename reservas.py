class Reserva:
    def __init__ (self,nro_reserva, mail,nro_habitacion, fecha_inicio, fecha_fin, tipo_habit,balcon,bano):
        self.mail=mail
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.balcon=balcon
        self.bano=bano
        self.tipo_habit=tipo_habit
        self.nro_reserva= nro_reserva
        self.nro_reserva= mail+str(fecha_inicio.date()) ######ver que hacer con esto#####
        self.nro_habitacion= nro_habitacion
        self.total=0