import subprocess
import re

def pingtodos():
    # Ejecutar ipconfig y obtener la salida
    ipconfig_output = subprocess.run('ipconfig', capture_output=True, text=True).stdout
    
    # Depuración: Imprimir la salida de ipconfig
    print(f"Salida de ipconfig:\n{ipconfig_output}")

    # Buscar la dirección IP
    ip_pattern = r'IPv4 Address[.\s]+:\s+(\d+\.\d+\.\d+\.\d+)'
    ip_match = re.search(ip_pattern, ipconfig_output)

    equipos = []

    if ip_match:
        ip_address = ip_match.group(1)
        # Obtener los primeros 3 octetos de la dirección IP
        network_prefix = '.'.join(ip_address.split('.')[:3])
        
        # Ejecutar arp -a y obtener la salida
        arp_output = subprocess.run('arp -a', capture_output=True, text=True).stdout
        
        # Depuración: Imprimir la salida de arp -a
        print(f"Salida de arp -a:\n{arp_output}")
        
        # Buscar todas las IPs en la misma red
        ip_list = re.findall(rf'{network_prefix}\.\d+', arp_output)
        
        print(f"IPs encontradas en la red {network_prefix}.0:")
        for ip in ip_list:
            # Usamos subprocess para capturar el resultado del ping
            ping_output = subprocess.run(['ping', '-a', ip], capture_output=True, text=True)
            if ping_output.returncode == 0:
                # Si el ping fue exitoso, se obtiene el nombre del host
                nombre = ping_output.stdout
                equipos.append(nombre)
                print(f"IP: {ip} -> {nombre}")
            else:
                print(f"IP {ip} no respondió al ping.")
    else:
        print("No se pudo encontrar la dirección IP.")

pingtodos()
