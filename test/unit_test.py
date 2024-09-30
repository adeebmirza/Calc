import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from app import app  # Make sure this points to where your app is defined

import unittest
from app import app  # Ensure the import points to the correct app file

class TestFlaskApp(unittest.TestCase):  # Class name starts with 'Test'
    
    # This runs before every test
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test the home page route '/'
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Calculator</title>', response.data)  # Check for the title tag
        self.assertIn(b'<h1 style="text-align: center">Calculator</h1>', response.data)  # Check for heading
        self.assertIn(b'<form action="/math" method="POST">', response.data)  # Check for the form element

    # Test the math operations with form data
    def test_math_operations_add(self):
        response = self.app.post('/math', data=dict(
            operation='add', num1=5, num2=3
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The sum of 5and 3is 8', response.data)

    def test_math_operations_sub(self):
        response = self.app.post('/math', data=dict(
            operation='subtract', num1=5, num2=3
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The subtract of 5and 3is 2', response.data)

    def test_math_operations_mul(self):
        response = self.app.post('/math', data=dict(
            operation='multiply', num1=5, num2=3
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The multiply of 5and 3is 15', response.data)

    def test_math_operations_(self):
        response = self.app.post('/math', data=dict(
            operation='divide', num1=9, num2=3
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The divide of 9and 3is 3', response.data)
    
if __name__ == '__main__':
    unittest.main()  # Ensure this is called to discover and run tests
