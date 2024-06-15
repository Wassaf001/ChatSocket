import socket
import threading

def handle_client(client_socket, client_address):
    print(f"New connection: {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{client_address}: {message}")
            broadcast(message, client_socket)
        except:
            client_socket.close()
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen()

clients = []

print("Server started, waiting for connections...")
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
