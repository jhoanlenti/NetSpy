import socket

def server_send_receive_data(host, port):
    # Crear el socket para el servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Vincular el socket al host y puerto
    server_socket.bind((host, port))
    
    # Escuchar conexiones entrantes
    server_socket.listen(1)
    print(f"Servidor escuchando en {host}:{port}...")

    # Crear un cliente que se conecta a sí mismo (simula una conexión)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    # Aceptar la conexión del cliente (en este caso será el socket cliente creado arriba)
    connection, address = server_socket.accept()

    # Recibir datos desde el cliente (en este caso, el socket cliente)
    data = connection.recv(1024)
    print(f"Servidor recibió: {data.decode('utf-8')}")
    
    # Enviar una respuesta al cliente (que es el mismo servidor en este caso)
    response = "Respuesta desde el servidor!"
    client_socket.send(response.encode('utf-8'))

    # Recibir la respuesta del servidor (en este caso, desde sí mismo)
    response_from_server = connection.recv(1024)
    print(f"Servidor recibió la respuesta: {response_from_server.decode('utf-8')}")

    # Cerrar la conexión
    connection.close()
    server_socket.close()
    client_socket.close()

# Configuración del servidor
host = '127.0.0.1'  # Escuchar en localhost
port = 12345         # Puerto para la conexión

# Iniciar el servidor que se conecta a sí mismo
server_send_receive_data(host, port)
