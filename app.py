# On importe le module Flask 

# /!\ On ajoute à l'import de flask le module render template
from flask import Flask, render_template

# On crée une instance d'application
app = Flask(__name__)

# On définit une route par défault
@app.route('/')
def bonjour():
    # Le retour de la route dans le navigateur sera Bonjour
    return "Bonjour"

# On définit une route pour afficher le résultat d'un template html
@app.route('/get_render')
def get_render():
# Les templates sont dans le dossier templates
    return render_template('get_render.html') # ATTENTION il faut redémarré l'application pour modifier le contenu du html

@app.route('/get_jinja')
def get_jinja():

    la_liste = ['Salut','Comment tu va?', 'bienvenue dans le monde magique de jinja!']
    return render_template('get_jinja.html', ma_list = la_liste)

#  Exécutez l'application si ce script est exécuté en tant que programme principal
if __name__ == '__main__':
    app.run()