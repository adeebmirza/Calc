import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from app import app  # Ensure the import points to the correct app file

# Set up the path for the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Calculator</title>' in response.data  # Check for the title tag
    assert b'<h1 style="text-align: center">Calculator</h1>' in response.data  # Check for heading
    assert b'<form action="/math" method="POST">' in response.data  # Check for the form element

def test_math_operations_add(client):
    response = client.post('/math', data=dict(
        operation='add', num1=5, num2=3
    ))
    assert response.status_code == 200
    assert b'The sum of 5and 3is 8' in response.data

def test_math_operations_subtract(client):
    response = client.post('/math', data=dict(
        operation='subtract', num1=5, num2=3
    ))
    assert response.status_code == 200
    assert b'The subtract of 5and 3is 2' in response.data

def test_math_operations_multiply(client):
    response = client.post('/math', data=dict(
        operation='multiply', num1=5, num2=3
    ))
    assert response.status_code == 200
    assert b'The multiply of 5and 3is 15' in response.data

def test_math_operations_divide(client):
    response = client.post('/math', data=dict(
        operation='divide', num1=9, num2=3
    ))
    assert response.status_code == 200
    assert b'The divide of 9and 3is 3' in response.data
