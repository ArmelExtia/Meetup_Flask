from flask import Blueprint,current_app
import random
api = Blueprint('api', __name__)

@api.route("/")
def test():
    choice = ["french","english","deutch"]


    Bonjour = current_app.config["hi"][random.choice(choice)]

    return Bonjour