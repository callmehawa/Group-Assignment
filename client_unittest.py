import unittest
from unittest.mock import patch, MagicMock
import Client  # Import the code you want to test

class TestClient(unittest.TestCase):

    @patch('Client.send_to_server', return_value=True)
    def test_send_file_to_server(self, mock_send_to_server):
        # Your test code here
        result = Client.send_file_to_server('test_file.txt')
        self.assertTrue(result)  # Check if the result is True, indicating a successful send

if __name__ == '__main__':
    unittest.main()
