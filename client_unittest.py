import unittest
from . import Client.py  # Import the code you want to test

class TestClient(unittest.TestCase):

    def test_write_and_load_key(self):
        # Test writing and loading the key
        Client.write_key()
        loaded_key = Client.load_key()
        self.assertIsNotNone(loaded_key)
        self.assertIsInstance(loaded_key, bytes)

    def test_encrypt_decrypt(self):
        # Test encryption and decryption
        key = Client.load_key()
        original_data = b"Test data to encrypt and decrypt"
        encrypted_data = Client.encrypt(original_data, key)
        self.assertIsNotNone(encrypted_data)
        self.assertNotEqual(encrypted_data, original_data)

        decrypted_data = Client.decrypt(encrypted_data, key)
        self.assertEqual(decrypted_data, original_data)

if __name__ == '__main__':
    unittest.main()
