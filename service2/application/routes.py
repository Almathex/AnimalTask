from flask import redirect, url_for, Response, request
from application import app
import requests
import random

@app.route('/')
@app.route('/animal/name', methods=['GET','POST'])
def animal_name():
    animal_list=["fish", "pig","parrot","dog", "sheep", "cat "]
    data = random.choice(animal_list)
    return Response(data, mimetype='text/plain')

@app.route('/animal/noise', methods=['GET','POST'])
def animal_noise():
    response=request.data.decode('utf-8')
    if response == "fish":
        noise = "Gulp"
    elif response == "pig":
        noise = "Oink"
    elif response == "parrot":
        noise = "Polly wants a cracker"
    elif response == "dog":
        noise = "Woof"
    elif response == "sheep":
        noise = "Baaa"
    elif response == "cat":
        noise = "Meow"    
    else:
        noise = "*Villager noises*"
    return Response(noise, mimetype='text/plain')
