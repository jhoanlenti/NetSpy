import os
import re

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

#print(equipos)