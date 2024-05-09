import socket

# Dirección y puerto del servidor
HOST = '127.0.0.1'  
PORT = 12345  

#  socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Conectar el socket al servidor
    client_socket.connect((HOST, PORT))
    # Enviar datos al servidor
    while True:
        mensaje = input("Ingrese un mensaje para enviar al servidor: ")
        if mensaje.lower() == "cerrar":
            break
        client_socket.sendall(mensaje.encode())
        data = client_socket.recv(1024)
        print('Respuesta del servidor:', data.decode())