# excepciones.py
# Módulo para definir excepciones personalizadas del sistema de gestión

class ErrorSistema(Exception):
    """Clase base para otras excepciones del sistema."""
    pass

class ValorInvalidoError(ErrorSistema):
    """Excepción para valores inválidos, como costos negativos o datos incorrectos."""
    def __init__(self, mensaje="Valor inválido proporcionado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ClienteNoEncontradoError(ErrorSistema):
    """Excepción cuando un cliente no se encuentra en el sistema."""
    def __init__(self, cliente_id=None, mensaje=None):
        if mensaje is None:
            mensaje = f"Cliente con ID '{cliente_id}' no encontrado" if cliente_id else "Cliente no encontrado"
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ServicioNoDisponibleError(ErrorSistema):
    """Se lanza cuando un servicio solicitado no está activo o disponible."""
    def __init__(self, mensaje="El servicio no se encuentra disponible actualmente."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class DatosInvalidosError(ErrorSistema):
    """Se lanza cuando los datos de entrada no cumplen con el formato requerido."""
    def __init__(self, campo, mensaje="Los datos proporcionados son inválidos."):
        self.campo = campo
        self.mensaje = f"Error en el campo '{campo}': {mensaje}"
        super().__init__(self.mensaje)

class ReservaConflictoError(ErrorSistema):
    """Excepción para conflictos en reservas, como fechas superpuestas."""
    def __init__(self, mensaje="Conflicto en la reserva"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ReservaInvalidaError(ErrorSistema):
    """Excepción para reservas inválidas, como fechas pasadas."""
    def __init__(self, mensaje="Reserva inválida"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        # buenas tardes 
        