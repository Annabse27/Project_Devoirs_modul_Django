from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """
    Page d'accueil de l'application.
    Cette fonction renvoie le template de la page d'accueil du site de catalogue de produits.
    """
    return render_template('index.html')

if __name__ == '__main__':

    """
    Point d'entrée de l'application Flask.
    L'application s'exécute en mode debug.
    """

    app.run(debug=True)

