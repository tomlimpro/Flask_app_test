from flask import Flask, render_template
import os
app = Flask(__name__)

os.environ['FLASK_ENV'] = 'development'

@app.route('/')
def index():
    return render_template('index.html')


"""
Permet de démarrer l'application uniquement lorsque le fichier est exécuté directement
et non lorsque le fichier est importé en tant que module dans un autre script.

La fonction 'app.run' a des paramètres opérationnels tels que 'host' et 'port' qui permettent de configurer
l'adresse ip et le numéro sur lesquels l'application écoutera les requêtes.
"""
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True)