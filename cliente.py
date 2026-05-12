from excepciones import ClienteError

class Cliente:
    def __init__(self, nombre, correo):
        self.set_nombre(nombre)
        self.set_correo(correo)

    # Encapsulación
    def set_nombre(self, nombre):
        if not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío")
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_correo(self, correo):

        if "@" not in correo:
            raise ClienteError("Correo inválido")
        self.__correo = correo

    def get_correo(self):
        return self.__correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - {self.__correo}"