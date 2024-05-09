import socket

HOST = '127.0.0.1'  
PORT = 12345  # 

# socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Enlazar el socket a la dirección y el puerto
    server_socket.bind((HOST, PORT))
    # Escuchar conexiones entrantes
    server_socket.listen()

    print('Esperando conexiones...')
    # Aceptar la conexión entrante
    conn, addr = server_socket.accept()
    with conn:
        print('Conectado a', addr)
        # Recibir datos del cliente
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Datos recibidos:', data.decode())
            # Envía una respuesta al cliente
            conn.sendall(b'Mensaje recibido correctamente por el servidor')