# On importe le module Flask 

# /!\ On ajoute à l'import de flask le module requests
from flask import Flask, render_template,request

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

# On définit une route pour afficher le résultat d'un template html avec un jinja
@app.route('/get_jinja')
def get_jinja():
    # On crée une liste de valeur qui sera renvoyé à jinja
    la_liste = ['Salut','Comment tu va?', 'bienvenue dans le monde magique de jinja!']
    # On retourne vers la page html 
    return render_template('get_jinja.html', ma_list = la_liste)

# On définit une route pour afficher un calculatrice
@app.route('/calculatrice', methods=['GET', 'POST'])
def calculatrice():
    # Le résultat par défault sera none 
    result = ""
    # Si la méthod est un post c'est que le formulaire a envoyé une demande
    if request.method == 'POST':
        # On récupère la valeur 1 depuis la requete envoyé
        num1 = float(request.form['num1'])
        # On récupère la valeur 2 depuis la requete envoyé
        num2 = float(request.form['num2'])
        # On récupère l'opérateur' depuis la requete envoyé
        operator = request.form['operator']
        # Si l'opérateur est ajout
        if operator == 'add':
            # Le résulatat renvoyé sera
            result = f"Résultat : {num1 + num2}"
        # Si l'opérateur est une soustration    
        elif operator == 'subtract':
            result = f" Résultat : {num1 - num2}"
        # Si l'opérateur est une multiplication
        elif operator == 'multiply':
            result = f"Résultat : {num1 * num2}"
        # Si l'opérateur est une division
        elif operator == 'divide':
            # Les division par zero sont impossible!!!
            if num2 != 0:
                result = f"Résultat : {num1 / num2}"
            else:
                result = "Division par zéro impossible"
    # Si la requete n'est pas un post mais un get ou autre chose a laquel nous n'aurions pas pensé :)
    else:
        # On ne fait rien
        pass
    # Dans tous les cas on renvoi la page de calcul
    return render_template('calculatrice.html', result=result)

#  Exécutez l'application si ce script est exécuté en tant que programme principal
if __name__ == '__main__':
    app.run()