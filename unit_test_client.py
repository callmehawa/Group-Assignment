import unittest
from unittest import mock
import Client

class TestClient(unittest.TestCase):

    def setUp(self):
        # Create a key file for testing
        with open("test_key.key", "wb") as key_file:
            key_file.write(b"test_key")

    def tearDown(self):
        # Clean up after the test by removing the test key file
        import os
        os.remove("test_key.key")

    def test_main(self):
        print("Testing the main function...")

        # Mock the functions and methods
        create_client_socket_mock = mock.MagicMock()
        connect_to_server_mock = mock.MagicMock()
        write_key_mock = mock.MagicMock()
        load_key_mock = mock.MagicMock(return_value=b"test_key")
        encrypt_mock = mock.MagicMock(return_value=b"encrypted_data")
        # Change the response from the server here
        receive_response_mock = mock.MagicMock(return_value="Connection successful")

        # Replace the functions and methods in the Client module with the mocks
        Client.create_client_socket = create_client_socket_mock
        Client.connect_to_server = connect_to_server_mock
        Client.write_key = write_key_mock
        Client.load_key = load_key_mock
        Client.encrypt = encrypt_mock
        Client.send_encrypted_data = mock.MagicMock()
        Client.receive_response = receive_response_mock

        # Call the main function
        Client.main()

        # Assertions to verify that functions and methods were called with the expected arguments
        create_client_socket_mock.assert_called_once()
        connect_to_server_mock.assert_called_once_with(create_client_socket_mock.return_value, ('localhost', 12345))
        write_key_mock.assert_called_once()
        load_key_mock.assert_called_once()
        encrypt_mock.assert_called_once_with(
            mock.ANY,  # Allow any serialized data argument here
            b"test_key"  # Ensure the key argument is correct
        )
        
        # Print the custom message from the client
        #print("Message from client:", receive_response_mock.return_value)

        # Print a test summary
        print("Test summary:")
        print("  - key generation, encryption and connection to server function was tested.")
        print("  - All mocked functions were called with the expected arguments.")
        print("  - Test completed successfully.")

if __name__ == '__main__':
    unittest.main()

