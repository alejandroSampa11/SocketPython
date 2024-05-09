import socket


def obtener_ip():
    # Obtener el nombre del host
    hostname = socket.gethostname()
    # Obtener la dirección IP asociada al nombre del host
    ip_address = socket.gethostbyname(hostname)
    return ip_address

print("La dirección IP del host es:", obtener_ip())

# Dirección y puerto del servidor  
HOST = obtener_ip()
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