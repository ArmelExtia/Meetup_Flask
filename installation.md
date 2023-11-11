Installation

Création de l'environnement virtuel
Téléchargez python3.
Une fois python3 installé sur votre poste créez l'environnement virtuel via :

py -m venv venv


L'environnement virtuel permettra d'installer des paquet uniquement dans cet environnement, et pas sur la machine.
Une fois l'environnement virtuel créé vous devriez voir apparaitre un répertoire venv.

Installation des paquets
Installez les paquets nécessaires directement dans l'environnement virtuel via :

venv\Scripts\python.exe -m pip install -r requirements.txt



Lancement de l'application
Une fois les paquets installés vous pouvez lancer l'application via :

venv\Scripts\python.exe app.py


Le terminal devrait vous afficher :

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-618-973


Vous pouvez maintenant vous rendre sur l'URL http://127.0.0.1:5000 depuis votre navigateur.