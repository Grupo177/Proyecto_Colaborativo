from abc import ABC, abstractmethod

#Creacion de la clase padre Servicio con nombre y costo base
class Servicio(ABC):
    def __init__(self, nombre_base, costo_base):
        self.nombre_base = nombre_base
        self.costo_base = costo_base

#metodo de tipo abstracto donde se pasa el argumento **Kwargs porque no se tiene conocimeinto la cantidad de argumentos que se van a incluir
    @abstractmethod
    def calcular_costo(self, **kwargs):
        pass

#Clase Hija ServicioTransporte y calcular el costo donde se envian los argumentos distancia e impuesto
class ServicioTrasporte(Servicio):
    def calcular_costo(self, distancia=1, impuesto=0.15):
        return(self.costo_base*distancia)/impuesto

#Clase hija ServicioAlojamiento y calcular el costo en base a los argumentos noches y descuento
class ServicioAlojamiento(Servicio):
    def calcular_costo(self, noches=1, descuento=0):
        return (self-self.costo_base*noches)/descuento

#Clase hija ServicioGuia y calcular el costo en bae al algumento personas
class ServicioGuia(Servicio):
    def calcular_costo(self, personas=1):
        return self.costo_base * personas