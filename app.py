from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
#inizializza l'app Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
   db.create_all()


lista_spesa= []
#rotta principale
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
   #ttiene elemento dal form
   elemento = request.form['elemento']
   #aggiunge alla lista
   if elemento:
      lista_spesa.append(elemento)
   return redirect(url_for('home'))
@app.route('/')
def home():
 return render_template('index.html', lista=lista_spesa)



@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
   if 0 <= indice < len(lista_spesa):
      lista_spesa.pop(indice)
      return redirect(url_for('home'))


@app.route('/svuota', methods=['POST'])
def svuota():
    global lista_spesa  
    lista_spesa.clear()  
    return redirect(url_for('home'))

#avvio dell'app Flask
if __name__ == '__main__':
 app.run(debug=True)