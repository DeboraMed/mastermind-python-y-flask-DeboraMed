from flask import *
import random
#app = Flask(__name__)
## parte de local server web con flask
app = Flask(__name__)

colores = {
    "Yellow": "#ffff00",
    "Black": "#000000",
    "Green": "#00ff00",
    "Red": "#ff0000",
    "Cyan": "#00ffff",
    "White": "#ffffff",
    "Purple": "#ff00ff",
    "Blue": "#0000ff"}

@app.route('/', methods=['GET','POST'])
def index():
   # no esta accesible
   data = {"titulo": "MasterMind"}
   return render_template('home.html',data=data, colores=colores,intento=intento,intentos_realizados=intentos_realizados)

# tutorial flask https://www.youtube.com/watch?v=-1DmVCPB6H8&t=333s

def nuevo_secreto(colores):
   secreto = ()
   
   for i in range(4):
      secreto.append(random.choice(list(colores.values())))
      
   return secreto

def calcula_resultado(intento,secreto):
   descolocados = 0
   acertados = 0
   for i in range(4):
      if intento[i] == secreto[i]:
         acertados=acertados+1
      if intento[i] in secreto:
         descolocados = descolocados+1
         
   return acertados,descolocados

def mastermind():
   data = {"titulo": "MasterMind"}
   
   if 'secreto' not in session:
      session['secreto']= nuevo_secreto(colores)
      session['intentos_realizados']=[]
   intento=[]
   intentos_realizados=session.get('intentos_realizados',[])
      
   if request.method=='POST':
      intento=request.form.getlist('intento[]')
      session['intentos']=session.get('intentos',0)+1
      resultado= calcula_resultado(intento,session['secreto'])
      intentos_realizados.append((session['intentos'],intento,resultado))
      session['intentos_realizados']=intentos_realizados
   
   return render_template('home.html',data=data, colores=colores,intento=intento,intentos_realizados=intentos_realizados)

def reiniciar():
   session.pop('secreto', None)
   session.pop('intentos', None)
   session.pop('intentos_realizados', None)
   
   return "Juego reiniciado"

if __name__ == '__main__':
   app.run(debug=True,port=5000)
   
