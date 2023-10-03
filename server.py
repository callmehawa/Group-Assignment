import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening on {}:{}".format(*server_address))

# Accept a connection
client_socket, client_address = server_socket.accept()
print("Accepted connection from {}:{}".format(*client_address))

try:
    # Receive data from the client
    data = client_socket.recv(1024)
    print("Received data: {}".format(data.decode('utf-8')))

    # Send a response back to the client
    response = "Hello, dicitionary received!"
    client_socket.send(response.encode('utf-8'))
finally:
    # Clean up the connection
    client_socket.close()
    server_socket.close()
