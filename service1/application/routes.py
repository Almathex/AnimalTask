  
from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title='Home')


@app.route('/get/animal', methods=['GET','POST'])
def animal():
    response = requests.get("http://service2:5000/animal")
    animal=requests.get('http://service2:5001/animal/name')
    noise=requests.post('http://service2:5001/animal/noise',data=animal.text)
    return render_template('animal.html',title='Animals', animal=animal.text, noise=noise.text)
