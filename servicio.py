from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre_base, costo_base):
        self.nombre_base = nombre_base
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, **kwargs):
        pass


class ServicioTrasporte(Servicio):
    def calcular_costo(self, distancia=1, impuesto=0.15):
        return(self.costo_base*distancia)/impuesto
    
class ServicioAlojamiento(Servicio):
    def calcular_costo(self, noches=1, descuento=0):
        return (self-self.costo_base*noches)/descuento
    
class ServicioGuia(Servicio):
    def calcular_costo(self, personas=1):
        return self.costo_base * personas