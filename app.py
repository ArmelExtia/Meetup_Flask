# On importe le module Flask
from flask import Flask

# On crée une instance d'application
app = Flask(__name__)

# On définit une route par défault
@app.route('/')
def bonjour():
    # Le retour de la route dans le navigateur sera Bonjour
    return "Bonjour"


#  Exécutez l'application si ce script est exécuté en tant que programme principal
if __name__ == '__main__':
    app.run()