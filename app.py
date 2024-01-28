# On importe le module Flask 

# /!\ On ajoute à l'import de flask le module url_for, redirect et session
from flask import Flask, render_template,request,url_for, redirect,session

# On crée une instance d'application
app = Flask(__name__)

# On définit une route par défault
@app.route('/')
def bonjour():
    # Le retour de la route dans le navigateur sera Bonjour
    return helloLang('fr')

# On définit une route paramétrique
@app.route('/hello/<string:lang>/')
def helloLang(lang):
    # Le retour de la route dans le navigateur sera Bonjour dans la langue choisie et disponible
    txt = ""
    if lang == 'fr':
        txt = "Bonjour"
    elif lang == 'en':
        txt = "Hello"
    elif lang == 'de':
        txt = "Guten Tag"
    return txt


######################
## AUTHENTIFICATION ##
######################

# On configure une clé secrete pour sécurisé l'application
app.config['SECRET_KEY'] = 'CleSecreteDeMalade!'

# On crée une route pour l'authentification
@app.route('/login', methods=['GET','POST'])
def login():
    # Si la méthode d'accès à la page est un post
    if request.method == 'POST':
        # On crée la session avec le nom utilisateur envoyé par l'utilisateur
        session['user'] = request.form['username']
        # Et on envoi à son tableau de bord
        return redirect(url_for('dashboardFct'))
    # Si la méthode d'accès à la page est un get on envoi la page html de login.
    return render_template('login.html')

# On crée une route pour le dashboard
@app.route('/dashboard')
def dashboardFct():
    # Si il y a un utilisateur connecté on lui présente son dashboard
    if 'user' in session:
        #La connexion est autorisée
        message = f"Bienvenue dans votre espace personnel {session['user']}!"
        return message
    # Autrement on le renvoie à la page de login
    return redirect(url_for('login'))

# On se fait une petite page de logout parce qu'on veut pouvoir se déconnecter.
@app.route('/logout')
def logout():
    # Si il y avait un utilisateur connecté
    if 'user' in session:
        # On le déconnecte
        session.pop('user',None)
        # On l'informe qu'il a bien été déconnecté
        return "Vous avez bien été déconnecté"
    # Autrement on se fou de lui.
    return "Vous n'etiez pas connecté, comment voulez vous que je vous déconnecte?"
















# On définit une route pour afficher le résultat d'un template html
@app.route('/get_render')
def get_render():
# Les templates sont dans le dossier templates
    return render_template('get_render.html') # ATTENTION il faut redémarrer l'application pour modifier le contenu du html

# On définit une route pour afficher le résultat d'un template html avec un jinja
@app.route('/get_jinja')
def get_jinja():
    # On crée une liste de valeur qui sera renvoyée à jinja
    la_liste = ['Salut', 'bienvenue dans le monde magique de jinja!','Comment tu vas?']
    # On retourne vers la page html 
    return render_template('get_jinja.html', ma_list = la_liste)

# On définit une route pour afficher un calculatrice
@app.route('/calculatrice', methods=['GET', 'POST'])
def calculatrice():
    if 'user' in session:
        # Le résultat par défault sera none 
        result = ""
        # Si la méthode est un post c'est que le formulaire a envoyé une demande
        if request.method == 'POST':
            # On récupère la valeur 1 depuis la requête envoyée
            num1 = float(request.form['num1'])
            # On récupère la valeur 2 depuis la requête envoyée
            num2 = float(request.form['num2'])
            # On récupère l'opérateur' depuis la requête envoyée
            operator = request.form['operator']
            # Si l'opérateur est une addition
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
                # Les divisions par zero sont impossibles!!!
                if num2 != 0:
                    result = f"Résultat : {num1 / num2}"
                else:
                    result = "Division par zéro impossible"
            # Puis on renvoie la page de calcul
            return render_template('calculatrice.html', result=result, num1Value=num1, ope=operator, num2Value=num2,utilisateur=session['user'])
        elif request.method == 'GET':
            # on renvoie la page de calcul
            return render_template('calculatrice.html', result=result,utilisateur=session['user'])
    else : 
        return redirect(url_for('login'))














#  Exécutez l'application si ce script est exécuté en tant que programme principal
if __name__ == '__main__':
    app.run()
