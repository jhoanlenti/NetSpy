import os
import re
from .os_check import sistema
from .stat_ports import comprobar_ip


# Función para validar si la entrada es una dirección IP válida
def is_valid_ip(ip):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(pattern, ip) is not None

# Función para verificar si la IP está activa mediante ping
def is_ip_active(ip):
    sis_os = sistema()
  
    if sis_os == "windows":
        response = os.system(f"ping -n 1 {ip} > nul 2>&1")
    elif sis_os == "linux":
        response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    else:
        return False
    
    return response == 0  # Si la respuesta es 0, significa que la IP está activa

def specificip():
    host2 = input("Introduce la IP a escanear: ")
    
    # Comprobamos que la IP sea válida
    while not is_valid_ip(host2):
        print("La dirección ingresada no es una IP válida.")
        host2 = input("Introduce la IP a escanear: ")
    
    # Verificar si la IP está activa
    if is_ip_active(host2):
        print(f"La IP {host2} está activa.")
        escanear = input("¿Deseas hacer un escaneo de esta IP? (s/n): ").strip().lower()
        if escanear == 's':
            print("Escaneando...")
            comprobar_ip(host2)
        else:
            print("Escaneo no realizado.")
    else:
        print(f"La IP {host2} no está activa.")
