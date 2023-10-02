#Client sevrer Network
"""Creating a client for a simple client server network which will serialise and ncrypt a string 
before sending it to the server"""

import socket
import pickle
#import json
from cryptography.fernet import Fernet

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

# Generate a key for encryption (you should store and share this key securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)
print(key)

try:
    # Send data to the server
    #message = "Hello, server!"

    # Add  a new dictionary
    dictionary = {"name": "Pawan", "age": 40, "city": "Preston"}

#creates new file to serialise into pickle
    with open('dict.pickle', 'wb') as file:
      pickle.dump(dictionary, file)

# Read the serialized data from the file
    with open('dict.pickle', 'rb') as file:
        serialised_data = file.read()
      
    # Serialize as JSON
    #json_data = json.dumps(dictionary)

    # Encrypt the JSON data
    encrypted_data = cipher_suite.encrypt(serialised_data)

    #send serialised dictionary to server

    client_socket.send(encrypted_data)

    # Receive a response from the server
    response = client_socket.recv(1024)
    print("Received response from server: {}".format(response.decode('utf-8')))
finally:
    # Clean up the connection
    client_socket.close()

# End-of-file (EOF)