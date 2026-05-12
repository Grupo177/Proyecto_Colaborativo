<<<<<<< Updated upstream
=======
class ErrorSistema(Exception):
    """Clase base para otras excepciones del sistema."""
    pass

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
        
        
        
        
        
>>>>>>> Stashed changes
