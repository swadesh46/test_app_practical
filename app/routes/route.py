from flask import Flask, Blueprint, current_app, jsonify
import os

app1=Blueprint('route1', __name__)

@app1.route('/')

def display():
    name=os.getenv('app_username')
    filename=current_app.config['app']['file']
    pswd=current_app.config['app']['pswd']

    return jsonify({'hello':filename + pswd})
    