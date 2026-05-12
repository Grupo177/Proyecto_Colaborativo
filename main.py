from cliente import Cliente
from servicio import ServicioTrasporte, ServicioAlojamiento, ServicioGuia
from reserva import Reserva
from excepciones import ClienteError, ReservaError, ErrorSistema
from logger import log_info, log_error

def ejecutar_sistema():
    """
    Función principal que integra todos los módulos y ejecuta 
    las 10 simulaciones requeridas por la guía.
    """
    log_info("Inicio del sistema de simulaciones.")
    print("=== SISTEMA INTEGRAL DE GESTIÓN DE VIAJES ===")

    # 1. Definición de Catálogo de Servicios
    vuelo_nacional = ServicioTrasporte("Vuelo Ruta A", 200.0)
    estadia_estandar = ServicioAlojamiento("Hospedaje Tipo B", 120.0)
    recorrido_cultural = ServicioGuia("Guía Turístico C", 50.0)

    # 2. Configuración de 10 Casos de Prueba (Simulaciones)
    # Incluye casos de éxito y casos diseñados para disparar excepciones
    simulaciones = [
        {"id": 1, "n": "Usuario Uno", "c": "user1@example.com", "s": vuelo_nacional, "d": 2, "cancelar": False},
        {"id": 2, "n": "Usuario Dos", "c": "user2@example.com", "s": estadia_estandar, "d": 3, "cancelar": False},
        {"id": 3, "n": "Usuario Tres", "c": "user3@example.com", "s": recorrido_cultural, "d": 1, "cancelar": False},
        {"id": 4, "n": "", "c": "error@mail.com", "s": vuelo_nacional, "d": 1, "cancelar": False}, # Error: Nombre vacío
        {"id": 5, "n": "Usuario Cinco", "c": "correo_invalido.com", "s": estadia_estandar, "d": 1, "cancelar": False}, # Error: Formato correo
        {"id": 6, "n": "Usuario Seis", "c": "user6@example.com", "s": recorrido_cultural, "d": 2, "cancelar": True}, # Error: Reserva cancelada
        {"id": 7, "n": "Usuario Siete", "c": "user7@example.com", "s": vuelo_nacional, "d": 0, "cancelar": False}, # Error: Lógica de cálculo
        {"id": 8, "n": "Usuario Ocho", "c": "user8@example.com", "s": estadia_estandar, "d": 4, "cancelar": False},
        {"id": 9, "n": "Usuario Nueve", "c": "user9@example.com", "s": recorrido_cultural, "d": 5, "cancelar": False},
        {"id": 10, "n": "Usuario Diez", "c": "user10@example.com", "s": vuelo_nacional, "d": 1, "cancelar": False}
    ]

    for simulacion in simulaciones:
        print(f"\n--- Ejecutando Simulación {simulacion['id']} ---")
        try:
            # Validación de datos del cliente 
            nuevo_cliente = Cliente(simulacion['n'], simulacion['c'])
            
            # Creación del registro de reserva
            nueva_reserva = Reserva(nuevo_cliente, simulacion['s'], simulacion['d'])
            
            if simulacion['cancelar']:
                nueva_reserva.cancelar()
                # Intento de confirmación forzada para disparar ReservaError
                nueva_reserva.confirmar() 
            else:
                nueva_reserva.confirmar()

            # Procesamiento final y cálculo de costos
            resultado = nueva_reserva.procesar()
            print(resultado)
            log_info(f"Éxito: Simulación {simulacion['id']} procesada.")

        except (ClienteError, ReservaError) as error_personalizado:
            print(f"ALERTA DEL SISTEMA: {error_personalizado}")
            log_error(error_personalizado)
        except Exception as error_general:
            print(f"FALLO CRÍTICO: {error_general}")
            log_error(f"Error no esperado en Simulación {simulacion['id']}: {error_general}")
        else:
            print(f"Simulación {simulacion['id']} completada satisfactoriamente.")
        finally:
            # Siempre se ejecuta, garantizando la continuidad del sistema [cite: 2]
            print(f"Finalización de rutina para Simulación {simulacion['id']}.")

    log_info("Fin del ciclo de simulaciones.")

if __name__ == "__main__":
    ejecutar_sistema()