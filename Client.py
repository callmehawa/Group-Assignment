
#Client sevrer Network
"""Creating a client for a simple client server network which will serialise and ncrypt a string 
before sending it to the server"""

import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

try:
    # Send data to the server
    message = "Hello, server!"
    client_socket.send(message.encode('utf-8'))

    # Receive a response from the server
    response = client_socket.recv(1024)
    print("Received response from server: {}".format(response.decode('utf-8')))
finally:
    # Clean up the connection
    client_socket.close()



import json
import pickle

# Create an empty dictionary
my_dict = {}

# Create a dictionary with key-value pairs
dictionary = {"name": "Pawan", "age": 40, "city": "Preston"}

#serialse my_dict to json format

#json_data = json.dumps(dictionary)
#print(json_data)

# Serialize the dictionary using pickle
with open("serialized_dict.pickle", "wb") as pickle_file:
    pickle.dump(dictionary, pickle_file)
    print(dictionary)