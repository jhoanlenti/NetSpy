import os
import re


decision = int(input("Decide which option do you want to run. 1. Ping all ips of the negtwork 2.Ping a specific ip: "))


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
    print("Here is the list of all ips in the network: ")
    print(os.system('arp -a'))
    
    ipselect = input("Enter the ip that you ant to ping: ")
    print(os.system(f"ping -a {ipselect}"))


while True:
    if decision == 1:
        pingtodos()
    elif decision == 2:
        specificip()
    else:
        decision = input("Error input, Enter 1 or 2")