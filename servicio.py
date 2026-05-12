from abc import ABC, abstractmethod

# Creacion de la clase padre Servicio con nombre y costo base 
class Servicio(ABC):
    def __init__(self, nombre_base, costo_base):
        self.nombre_base = nombre_base
        self.costo_base = costo_base

    # Metodo abstracto para asegurar que cada hija implemente su propio calculo 
    @abstractmethod
    def calcular_costo(self, cantidad=1):
        pass

# Clase Hija ServicioTransporte: Se ajusta la formula para evitar errores 
class ServicioTrasporte(Servicio):
    def calcular_costo(self, cantidad=1, impuesto=0.15):
        # Se suma el impuesto al costo base multiplicado por la distancia (cantidad)
        return (self.costo_base * cantidad) * (1 + impuesto)

# Clase hija ServicioAlojamiento: Se corrige el error de "self" y division por cero 
class ServicioAlojamiento(Servicio):
    def calcular_costo(self, cantidad=1, descuento=0):
        # Se elimina el 'self-' que rompia el codigo y se resta el descuento 
        return (self.costo_base * cantidad) - descuento

# Clase hija ServicioGuia: Se mantiene la logica de multiplicar por personas 
class ServicioGuia(Servicio):
    def calcular_costo(self, cantidad=1):
        return self.costo_base * cantidad