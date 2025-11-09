from flask import Flask, Blueprint
from dotenv import load_dotenv
import yaml
import os

def create_app():
    load_dotenv()
    app=Flask(__name__)
    config_path=os.path.join(os.getcwd(),'config','config.yaml')
    with open(config_path,'r') as f:
        config=yaml.safe_load(f)

    app.config.update(config)

    from app.routes.route import app1
    from app.routes.routes1 import app2
    app.register_blueprint(app1)
    app.register_blueprint(app2)
    return app




