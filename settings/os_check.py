import platform
from Banner.welcome import *

def sistema():
    try:
        sistema = platform.system()
    except Exception as e:
        print(f"Error al detectar el sistema operativo: {e}")
    else:
        if sistema == "Windows":
            print("El sistema operativo es Windows")   
        elif sistema == "Linux":
            print("El sistema operativo es Linux")
        else:
            print(f"Sistema operativo desconocido: {sistema}")
