from excepciones import ReservaError

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        if self.estado == "Cancelada":
            raise ReservaError("No se puede confirmar una reserva cancelada")
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        try:
            # Se usa el argumento genérico 'cantidad' para conectar con servicio.py
            costo = self.servicio.calcular_costo(cantidad=self.duracion)

            return f"""
Reserva procesada
Cliente: {self.cliente.get_nombre()}
Servicio: {self.servicio.nombre_base}
Costo: ${costo}
Estado: {self.estado}
"""
        except Exception as e:
            # Se incluye 'e' para ver el motivo real del fallo en la terminal
            raise ReservaError(f"Error al procesar reserva: {e}")