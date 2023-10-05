import os
import json
from flask import Flask


# Permet de récupérer la configuration
def getConf():
	data = {}
	with open(os.path.dirname(os.path.realpath(__file__)) + "/conf/configuration.json", encoding="utf-8") as json_file:
		data = json.load(json_file)
	return data



def create_app():
    app = Flask(__name__)
    configurations = getConf()
    for conf in configurations:
        app.config[conf] = configurations[conf]
		
    from .api.routes import api
	
    app.register_blueprint(api)
    
    return app