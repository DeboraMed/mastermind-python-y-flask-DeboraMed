from flask import *
from mastermind import *
app = Flask(__name__)
## parte de local server web con flask
app.secret_key = b'MI_CLAVE_SECRETA'

@app.route('/', methods=['GET','POST'])
def index():
 
      # Si existen datos en la sesión continúa el juego, si no crea nueva combinación
   if not 'secreto' in session:
      session['secreto'] = nuevo_secreto(colores)

   if request.method == 'POST':
      intento = request.form.getlist('intento[]')
      session['intento'] = intento

      # Recupera el historico previo de la sesion
      if not 'historico' in session:
         historico = []
      else:
         historico = session['historico']

      # Añade el resultado actual al historico de turnos
      historico.append(calcula_historico(intento,session['secreto']))
      # Almacena el estado del historico en la sesion
      session['historico'] = historico
      
   return render_template('home.html',colores=colores)

@app.post('/reset')
def reiniciar():
   session.pop('secreto', None)
   session.pop('intento', None)
   session.pop('historico', None)
   return redirect(url_for('index'))
   


if __name__ == '__main__':
   app.run(debug=True,port=5000)
   
