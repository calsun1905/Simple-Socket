import socket
import random

# Server configuration
server_ip = "127.0.0.1"
server_port = 4337
number_to_guess = random.randint(1, 10)

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"Server listening on {server_ip}:{server_port}")

# Accept connection from client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Game logic
attempts = 3
while attempts > 0:
    guess = int(client_socket.recv(1024).decode())
    print(f"Client's guess: {guess}")

    if guess == number_to_guess:
        client_socket.send("Win".encode())
        break
    elif guess < number_to_guess:
        client_socket.send("GreaterThan".encode())
    else:
        client_socket.send("LessThan".encode())

    attempts -= 1

# Close sockets
client_socket.close()
server_socket.close()
