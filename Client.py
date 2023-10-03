import socket
import pickle
from cryptography.fernet import Fernet

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

def write_key():
    """
<<<<<<< HEAD
    Generate a cryptographic key and save it to a file.

    This function generates a Fernet key and saves it to a file named 'key.key' in binary format.
=======
    Generating a key and saving it into a file
>>>>>>> aa1387a7156746feb3b324a8ccf30afdd7193c68
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
<<<<<<< HEAD
    Load the cryptographic key from the 'key.key' file.

    Returns:
        bytes: The Fernet key loaded from the 'key.key' file.
=======
    Loading the key from the current directory named `key.key`
>>>>>>> aa1387a7156746feb3b324a8ccf30afdd7193c68
    """
    return open("key.key", "rb").read()

# Generate and write a new key
write_key()

# Load the previously generated key
key = load_key()
print(f"Fernet Key: {key.hex()}")

# Call the print_key function to print the key
<<<<<<< HEAD
load_key()
=======
write_key()
>>>>>>> aa1387a7156746feb3b324a8ccf30afdd7193c68

try:
    # Add a new dictionary
    dictionary = {"name": "Pawan", "age": 40, "city": "Preston"}

    # Create a file to serialize into pickle
    with open('dict.pickle', 'wb') as file:
        pickle.dump(dictionary, file)

    # Read the serialized data from the file
    with open('dict.pickle', 'rb') as file:
        serialised_data = file.read()

    def encrypt(data, key):
        """
<<<<<<< HEAD
        Encrypt data using a Fernet key.

        Args:
            data (bytes): The data to be encrypted.
            key (bytes): The Fernet key used for encryption.

        Returns:
            bytes: The encrypted data.
=======
        Given data (bytes) and key (bytes), it encrypts the data and returns it
>>>>>>> aa1387a7156746feb3b324a8ccf30afdd7193c68
        """
        f = Fernet(key)
        encrypted_data = f.encrypt(data)
        return encrypted_data

    # Encrypt the serialized data
    encrypted_data = encrypt(serialised_data, key)

    # Send encrypted data to the server
    client_socket.send(encrypted_data)

    # Receive a response from the server
    response = client_socket.recv(1024)
    print(f"Message from server: {response.decode('utf-8')}")

<<<<<<< HEAD
finally:
    # Clean up the connection
    client_socket.close()
=======

finally:
    # Clean up the connection
    client_socket.close()
>>>>>>> aa1387a7156746feb3b324a8ccf30afdd7193c68
