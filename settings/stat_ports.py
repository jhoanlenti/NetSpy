import socket
import re
import threading
from queue import Queue
import time

# Diccionario con los puertos comunes y sus servicios según la IANA
PORTS = {
    20: "FTP Data Transfer",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    110: "POP3",
    143: "IMAP",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC",
    # ... puedes agregar más puertos y servicios según sea necesario
}

# Función para comprobar si un puerto está abierto
def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((host, port))
        return result == 0
    finally:
        sock.close()

# Función que será ejecutada por cada hilo
def port_scan_worker(host, port_queue, results):
    while not port_queue.empty():
        port = port_queue.get()
        if is_port_open(host, port):
            service = PORTS.get(port, "Desconocido")
            results.append(f"El puerto {port} está abierto en {host}. Servicio: {service}")
        port_queue.task_done()

# Función principal de escaneo
def scan_ports(host, num_threads=100):
    port_queue = Queue()
    results = []

    # Poner todos los puertos en la cola
    for port in range(1, 65536):
        port_queue.put(port)

    # Crear y iniciar los hilos
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=port_scan_worker, args=(host, port_queue, results))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    # Esperar a que todos los hilos terminen
    port_queue.join()

    # Imprimir resultados
    for result in sorted(results):
        print(result)

# Solicitar la IP al usuario y ejecutar el escaneo
def comprobar_ip(host):
    start_time = time.time()
    scan_ports(host)
    end_time = time.time()
    print(f"Escaneo completado en {end_time - start_time:.2f} segundos")