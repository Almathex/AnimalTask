from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from requests.api import request
import requests
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimals(TestBase):
    def test_animal(self):
        animal_list=[b"fish", b"pig", b"parrot", b"dog", b"sheep", b"cat"]
        response = self.client.get(url_for('animal_name'))
        self.assertIn(response.data, animal_list)

    def test_noise_duck(self):
        response =self.client.post(
            url_for('animal_noise'),
            data='fish',
        
        )
        self.assertIn(b'Gulp', response.data)
    def test_noise_pig(self):
        response =self.client.post(
            url_for('animal_noise'),
            data='pig',
            
        )
        self.assertIn(b'Oink', response.data)  
    def test_noise_parrot(self):
        response =self.client.post(
            url_for('animal_noise'),
            data='parrot',
            
        )
        self.assertIn(b'Polly wants a cracker', response.data)
    def test_noise_dog(self):
        response =self.client.post(
            url_for('animal_noise'),
            data='dog'
           
        )
        self.assertIn(b'Woof', response.data)
    def test_noise_sheep(self):
        response =self.client.post(
            url_for('animal_noise'),
            data='sheep'
        )
        self.assertIn(b'Baaa',response.data)
    def test_noise_cat(self):
        response =self.client.post(
            url_for('animal_noise'),
            data='cat'
        )    
        self.assertIn(b'Meow',response.data)    
    def test_noise_huh(self):
        response =self.client.post(
            url_for('animal_noise'),
            data='Rickard'
        )    
        self.assertIn(b'huh?',response.data)    
