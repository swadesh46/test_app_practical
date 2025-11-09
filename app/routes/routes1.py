from flask import Flask, Blueprint, current_app

app2=Blueprint('app2',__name__)

@app2.route('/hello')
def display():
    pswd=current_app.config['app']['pswd']
    return pswd