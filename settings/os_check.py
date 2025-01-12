import platform

def sistema():
    try:
        sistema = platform.system()
    except Exception as e:
        print(f"Error al detectar el sistema operativo: {e}")
    else:
        if sistema == "Windows":
            return "windows" 
        elif sistema == "Linux":
            return "linux"
        else:
            print(f"Sistema operativo desconocido: {sistema}")
