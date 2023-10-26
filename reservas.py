class Reserva:
    def __init__ (self, cliente, dni, fecha_inicio, fecha_fin, cant_personas, tipo_habit):
        self.cliente=cliente
        self.dni=dni
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.cant_personas=cant_personas 
        self.precio=tipo_habit.precio
        self.nro_reserva= dni+fecha_inicio