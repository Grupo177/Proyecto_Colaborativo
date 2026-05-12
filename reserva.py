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

            costo = self.servicio.calcular_costo(self.duracion)

            return f"""
Reserva procesada
Cliente: {self.cliente.get_nombre()}
Servicio: {self.servicio.nombre}
Costo: ${costo}
Estado: {self.estado}
"""

        except Exception as e:
            raise ReservaError("Error al procesar reserva") from e