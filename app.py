from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import get_db
app = Flask(__name__)
app.config['DATABASE'] = 'base_de_donnees.db'


def json_to_html_table(data):
    """Convertit une liste de dictionnaires en tableau HTML"""
    if not data:
        return "<p>Aucune donnée disponible</p>"
    
    # Commencer le tableau
    html = '<table border="1" style="border-collapse: collapse; width: 100%;">\n'
    
    # En-têtes
    html += '  <thead>\n    <tr>\n'
    for key in data[0].keys():
        html += f'      <th style="padding: 8px; background-color: #f2f2f2;">{key}</th>\n'
    html += '    </tr>\n  </thead>\n'
    
    # Corps du tableau
    html += '  <tbody>\n'
    for item in data:
        html += '    <tr>\n'
        for value in item.values():
            html += f'      <td style="padding: 8px;">{value}</td>\n'
        html += '    </tr>\n'
    html += '  </tbody>\n'
    html += '</table>'
    
    return html


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/etudiant")
def etudiant():
    return render_template("etudiants.html")

@app.route("/etudiant/emploi_du_temps", methods=['GET'])
def emploi_du_temp():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM L1GI_emploi ORDER BY id')
    entries = cursor.fetchall()
    db.close()
    entries_list = []
    for entry in entries:
        entries_list.append({
            'heure': entry[1],
            'lundi': entry[2],
            'mardi': entry[3],
            'mercredi': entry[4],
            'jeudi': entry[5],
            'vendredi': entry[6],
            'samedi': entry[7]
        })
    return render_template("emploi.html", emploi=entries_list)

@app.route("/etudiant/annonces", methods=["GET"])
def annonces():
    db= get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM L1GI_annonce ORDER BY date DESC')
    annonces= cursor.fetchall()
    db.close()
    annonces_list = []
    for annonce in annonces:
        annonces_list.append({
            'texte': annonce[1],
            'date': annonce[2]
        })
    return render_template("annonces.html", annonces=annonces_list)

@app.route("/etudiant/emploi_du_temps_page")
def emploi_du_temp_page():
    return render_template("emploi.html") 


@app.route("/prof")
def prof():
    return render_template("professeurs.html")
@app.route("/admin")
def admin():
    return render_template("administration.html")



if __name__ == "__main__":
    app.run(debug=True)