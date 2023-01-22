from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
import psycopg2

conn = psycopg2.connect(database="mydb", user="user", password="password", host="db")
cursor = conn.cursor()
app = Flask(__name__)
# Connexion à la base de donnée
engine = create_engine("postgresql://user:password@db:5432/mydb")
db=scoped_session(sessionmaker(bind=engine))

@app.route('/')
@app.route('/home')
def home_page():
    
    return render_template('home.html')

# Test pour récuperer des items manuellement
@app.route('/market')
def market_page():
    items = [
        {'id': 1,'name':'Phone', 'barcode': '35445231','price': 500},
        {'id': 2,'name':'Laptop', 'barcode': '85421221','price': 900},
        {'id': 3,'name':'Keyboard', 'barcode': '92541371','price': 150},
        {'id': 4,'name':'Mouse', 'barcode': '56541271','price': 50},
    ]
    
    return render_template('market.html', items=items)

@app.route('/playground')
def playground_page():
       return render_template('playground.html')

@app.route('/list_user', methods=["GET"])
def list_user():
    cursor.execute("SELECT * FROM USERS;")
    result = cursor.fetchall()
    return render_template('list_user.html', data=result)
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