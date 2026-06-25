from flask import Flask
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to Flatiron cars</h1>'

@app.route('/<string:model>')
def show_model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'