import datetime

def registrar_log(nivel, mensaje):
    """
    Gestiona el registro de eventos en logs.txt.
    Usa la estructura completa de control de excepciones.
    """
    archivo = None
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea_log = f"[{timestamp}] {nivel.upper()}: {mensaje}\n"
    
    try:
        # Intentamos abrir el archivo en modo 'append' (agregar)
        archivo = open("logs.txt", "a", encoding="utf-8")
    except IOError as e:
        print(f"CRITICAL: No se pudo escribir en el log. Error de E/S: {e}")
    else:
        # Se ejecuta solo si no hubo excepción al abrir el archivo
        archivo.write(linea_log)
    finally:
        # Se asegura de cerrar el recurso si fue abierto
        if archivo:
            archivo.close()

def log_error(excepcion):
    """Registra una excepción específica."""
    registrar_log("ERROR", str(excepcion))

def log_info(mensaje):
    """Registra información general."""
    registrar_log("INFO", mensaje)
    