import os

def get_ips_from_arp():
    """
    Obtiene las direcciones IP de la tabla ARP usando `os.popen()` con el comando `arp -a`.
    """
    ips = []
    # Ejecuta el comando `arp -a` y lee su salida
    with os.popen("arp -a") as arp_output:
        for line in arp_output:
            # Divide las líneas en palabras
            parts = line.split()
            if len(parts) > 1:
                # La primera parte suele ser la dirección IP
                ip = parts[0]
                if ip.count(".") == 3:  # Comprueba que es una dirección IPv4 válida
                    ips.append(ip)
    return ips

def ping_ip(ip):
    """
    Hace ping a una IP usando `os.system()` y devuelve True si responde.
    """
    # Ejecuta el comando ping y redirige la salida al null para ocultarla
    response = os.system(f"ping -n 1 -w 100 {ip} >nul 2>&1")
    return response == 0  # Si el código de salida es 0, la IP respondió

def main():
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

if __name__ == "__main__":
    main()