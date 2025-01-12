import time
import itertools
import string


# Iniciar funcion titulo
def wifi_hack_titulo():
    banner = f"""
        ██╗    ██╗██╗███████╗██╗     ██╗  ██╗ █████╗  ██████╗██╗  ██╗
        ██║    ██║██║██╔════╝██║     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
        ██║ █╗ ██║██║█████╗  ██║     ███████║███████║██║     █████╔╝ 
        ██║███╗██║██║██╔══╝  ██║     ██╔══██║██╔══██║██║     ██╔═██╗ 
        ╚███╔███╔╝██║██║     ██║     ██║  ██║██║  ██║╚██████╗██║  ██╗
         ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                        Security Tool | WIFI HACK           
                        Author: Jordi, Sergi, Ethan, Johan y Nuria                   
    """
    print(banner)

# Llamar funcion titulo
wifi_hack_titulo()


# Es un simulador de hackeo de fuerza bruta a una password wifi
# - Recomiendo para ver su funcionamiento rapidamente introducir una password de 3 caracteres
# - La variable password tendra la contraseña que se intentara hackear
# - La variable max_longitud sera la variable del tamaño maximo de la password
def hack_password(password, max_longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    intentos = 0
    inicio = time.time()
    
    for longitud in range(1, max_longitud + 1):
        for intento in itertools.product(caracteres, repeat=longitud): # Intertools genera combinaciones de caracteres posibles
            intentos += 1
            intento_actual = ''.join(intento)
            print(f"Finding... : {intento_actual}", end='\r')  # Actualiza el print en la misma linea
            if intento_actual == password:
                tiempo_total = time.time() - inicio
                print(f"\n[ÉXITO] Contraseña encontrada: '{password}' después de {intentos} intentos y {tiempo_total:.2f} segundos.")
                return

    print("\n[ERROR] No esta la contraseña en el rango prestablecido")

# Entrada al simulador
averiguar_contraseña = input("Introduce una contraseña ramdom para iniciar el simulador de Hackeo (maximo 8 caracteres): ")
hack_password(averiguar_contraseña)
