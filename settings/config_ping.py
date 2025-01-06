import os
import re
from .stat_ports import *

# Función para validar si la entrada es una dirección IP válida
def is_valid_ip(ip):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(pattern, ip) is not None

def pingtodos():
    # Ejecutar ipconfig y obtener la salida
    ipconfig_output = os.popen('ipconfig').read()

    # Buscar la dirección IP
    ip_pattern = r'IPv4 Address[.\s]+:\s+(\d+\.\d+\.\d+\.\d+)'
    ip_match = re.search(ip_pattern, ipconfig_output)

    equipos = []

    if ip_match:
        ip_address = ip_match.group(1)
        # Obtener los primeros 3 octetos de la dirección IP
        network_prefix = '.'.join(ip_address.split('.')[:3])
        
        # Ejecutar arp -a y obtener la salida
        arp_output = os.popen('arp -a').read()
        
        # Buscar todas las IPs en la misma red
        ip_list = re.findall(rf'{network_prefix}\.\d+', arp_output)
        
        print(f"IPs encontradas en la red {network_prefix}.0:")
        for ip in ip_list:
            nombre = os.system(f"ping -a {ip}")
            equipos.append(nombre)
    else:
        print("No se pudo encontrar la dirección IP.")

def specificip():
    host2 = input("Introduce la IP a escanear: ")
    
    while not is_valid_ip(host2):
        print("La dirección ingresada no es una IP válida.")
        host = input("Introduce la IP a escanear: ")
    
    #print(os.system(f"ping -a {ipselect}"))
    
    comprobar_ip(host2)

def mode():
    print(f"Escoge que opcion prefieres:\n")
    print(f"1. Buscar IP's de mi red activas")
    print(f"2. Analizar IP's si esta activa")
    decision = int(input("--> "))
    while True:
        if decision == 1:
            pingtodos()
        elif decision == 2:
            specificip()
        elif decision == 3:
            print(f"En proceso")
            #ip_public()
        else:
            decision = input("Error input, Enter 1, 2 or 3")