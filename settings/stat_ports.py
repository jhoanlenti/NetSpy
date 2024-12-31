import subprocess
import socket

# Función para comprobar si un puerto está abierto
def is_port_open(host, port):
    try:
        # Ejecutar el comando netcat para verificar si el puerto está abierto
        result = subprocess.run(
            ['nc', '-zv', host, str(port)], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        # Si el comando tiene salida en stdout que indica que el puerto está abierto
        if 'succeeded' in result.stdout.decode('utf-8'):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al comprobar el puerto {port}: {e}")
        return False

# Función para escanear un rango de puertos
def scan_ports(host, start_port, end_port):
    print(f"Escaneando puertos en {host} desde {start_port} hasta {end_port}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        if is_port_open(host, port):
            print(f"Puerto {port} está abierto.")
            open_ports.append(port)
    return open_ports

# Solicitar la IP del host
host = input("Introduce la IP o dominio a escanear: ")
# Definir el rango de puertos a escanear
start_port = 1
end_port = 1024

# Escanear los puertos
open_ports = scan_ports(host, start_port, end_port)

if open_ports:
    print(f"Puertos abiertos encontrados: {open_ports}")
else:
    print("No se encontraron puertos abiertos.")


####################
import socket

# Función para comprobar si un puerto está abierto
def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crear un socket TCP
    sock.settimeout(1)  # Establecer un tiempo de espera de 1 segundo
    try:
        sock.connect((host, port))  # Intentar conectar al host y puerto
        return True
    except (socket.timeout, socket.error):  # Si hay un error de conexión, el puerto está cerrado
        return False
    finally:
        sock.close()  # Cerrar el socket

# Solicitar la IP y puerto al usuario
host = input("Introduce la IP o dominio a escanear: ")
port = int(input("Introduce el puerto a comprobar: "))

# Verificar si el puerto está abierto
if is_port_open(host, port):
    print(f"El puerto {port} está abierto en {host}.")
else:
    print(f"El puerto {port} está cerrado en {host}.")
