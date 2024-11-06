import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        # Set up a test client
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Flask!', response.data)

if __name__ == "__main__":
    unittest.main()
