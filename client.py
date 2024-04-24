import socket

# Client configuration
server_ip = "127.0.0.1"
server_port = 4337

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Game loop
for _ in range(3):
    guess = int(input("Enter your guess (1-10): "))
    client_socket.send(str(guess).encode())

    response = client_socket.recv(1024).decode()
    print(f"Server's response: {response}")

    if response == "Win":
        print("Congratulations! You guessed the number.")
        break
    elif response == "GreaterThan":
        print("Your guess is greater than the number.")
    elif response == "LessThan":
        print("Your guess is less than the number.")
    else:
        print("Invalid response from the server.")

# Close socket
client_socket.close()
