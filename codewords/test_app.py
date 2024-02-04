import unittest
import json
from app import create_app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        
        """Set up a test client before each test."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_get_action_by_codeword(self):
        """Test getting an action ID by codeword."""
        response = self.client.get('/action/by_codeword/5001')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], 'alert')

    def test_get_codewords_by_id(self):
        """Test getting codewords by action ID."""
        response = self.client.get('/action/by_id/proceed')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(5003, data['codewords'])  # Check if one of the expected codewords is in the response

if __name__ == '__main__':
    unittest.main()
