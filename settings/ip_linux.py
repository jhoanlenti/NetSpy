import os

def get_ips_from_arp():
    """
    Obtiene las direcciones IP de la tabla ARP usando `ip neigh`.
    """
    ips = []
    # Ejecuta el comando `ip neigh` para listar las entradas de la tabla ARP
    with os.popen("ip neigh") as arp_output:
        for line in arp_output:
            # Cada línea contiene la IP como el primer elemento
            parts = line.split()
            if len(parts) > 0:
                ip = parts[0]
                if ip.count(".") == 3:  # Verifica que sea una dirección IPv4
                    ips.append(ip)
    return ips

def ping_ip(ip):
    """
    Hace ping a una IP usando `os.system()` y devuelve True si responde.
    """
    response = os.system(f"ping -c 1 -w 100 {ip} > /dev/null 2>&1")
    return response == 0  

def lista_ips_lin():
    # Obtiene las IPs de la tabla ARP
    print("Obteniendo direcciones IP de la tabla ARP...")
    ips = get_ips_from_arp()
    print(f"Se encontraron {len(ips)} direcciones IP en la red.")

    # Lista para guardar las IPs que responden al ping
    active_ips = []

    # Realiza ping a cada IP
    print("Realizando ping a las direcciones IP encontradas...")
    for ip in ips:
        if ping_ip(ip):
            active_ips.append(ip)

    # Muestra las IPs activas
    print("\nDirecciones IP activas:")
    for ip in active_ips:
        print(ip)