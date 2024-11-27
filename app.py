from flask import Flask, render_template

#inizializza l'app Flask
app = Flask(__name__)
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

#avvio dell'app Flask
if __name__ == '__main__':
 app.run(debug=True)