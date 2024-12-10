from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, ListaSpesa

#inizializza l'app Flask
app = Flask(__name__)

#configura db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

#crea il db nel caso non esistesse anora
with app.app_context():
   db.create_all()


lista_spesa= []
#rotta principale


@app.route('/')
def home():
 return render_template('index.html', lista=lista_spesa)

 

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
   elemento = request.form['elemento']
   if elemento:
      lista_spesa.append(elemento)
      db.session.add(nuovo_elemento) 
      db.session.commit() 
   return redirect(url_for('home'))



@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
   if 0 <= indice < len(lista_spesa):
      lista_spesa.pop(indice)
      db.session.delete(elemento) 
      db.session.commit() 
      return redirect(url_for('home'))


@app.route('/svuota', methods=['POST'])
def svuota():
    lista_spesa.clear()  
    db.session.commit() #COMMENTA ???
    return redirect(url_for('home'))

#avvio dell'app Flask
if __name__ == '__main__':
 app.run(debug=True)