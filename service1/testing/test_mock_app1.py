from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from requests.api import request
import requests
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
     
    def test_get_fish(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "fish"
                p.return_value.text = "Gulp"

                response = self.client.get(url_for('animal'))
                self.assertIn(b'fish', response.data)
                self.assertIn(b'Gulp', response.data)
                self.assertEqual(response.status_code, 200)
          
    def test_get(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "pig"
                p.return_value.text = "Oink"

                response = self.client.get(url_for('animal'))
                self.assertIn(b'pig', response.data)
                self.assertIn(b'Oink', response.data)
                self.assertEqual(response.status_code, 200)          

    def test_get(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "parrot"
                p.return_value.text = "Polly wants a cracker"

                response = self.client.get(url_for('animal'))
                self.assertIn(b'parrot', response.data)
                self.assertIn(b'Polly wants a cracker', response.data)
                self.assertEqual(response.status_code, 200)

    def test_get(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "dog"
                p.return_value.text = "Woof"

                response = self.client.get(url_for('animal'))
                self.assertIn(b'dog', response.data)
                self.assertIn(b'Woof', response.data)
                self.assertEqual(response.status_code, 200)

    def test_get(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "sheep"
                p.return_value.text = "Baaa"

                response = self.client.get(url_for('animal'))
                self.assertIn(b'sheep', response.data)
                self.assertIn(b'Baaa', response.data)
                self.assertEqual(response.status_code, 200)

    def test_get(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "cat"
                p.return_value.text = "Meow"

                response = self.client.get(url_for('animal'))
                self.assertIn(b'cat', response.data)
                self.assertIn(b'Meow', response.data)
                self.assertEqual(response.status_code, 200)                
