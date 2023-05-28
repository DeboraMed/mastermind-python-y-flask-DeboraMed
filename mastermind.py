from flask import *
import random
#app = Flask(__name__)
## parte de local server web con flask

colores = {
    "Yellow": "#ffff00",
    "Black": "#000000",
    "Green": "#00ff00",
    "Red": "#ff0000",
    "Cyan": "#00ffff",
    "White": "#ffffff",
    "Purple": "#ff00ff",
    "Blue": "#0000ff"}

# tutorial flask https://www.youtube.com/watch?v=-1DmVCPB6H8&t=333s

def nuevo_secreto(colores):
   secreto = []
   
   for _ in range(4):
      secreto.append(random.choice(list(colores.values())))
      
   return secreto

def calcula_resultado(intento,secreto):
   descolocados = 0
   acertados = 0
   for i in range(4):
      if intento[i] == secreto[i]:
         acertados=acertados+1
         continue
      if intento[i] in secreto:
         descolocados = descolocados+1
         
   return "Acertados: " + str(acertados) + "   Descolocados: " + str(descolocados)

# Devuelve un array de colores donde 'red' es que no está, 'green' cuando es acierto
# y 'yellow' cuando no esta en su sitio
def calcula_aciertos(intento,secreto):
   estadoPosiciones = ['red','red','red','red']

   for i in range(4):
      if(intento[i] == secreto[i]):
         estadoPosiciones[i] = 'green'
         continue
      if(intento[i] in secreto):
         estadoPosiciones[i] = 'yellow'
   return estadoPosiciones

# Genera el HTML correspondiente a una entrada del historico
def calcula_historico(intento,secreto):
    resumenTurnoActual = '<div>'

    # Obtiene el estado de cada posicion (en codigo de colores)
    estadoPosiciones = calcula_aciertos(intento, secreto)

    for i in range(4):
        resumenTurnoActual += "<input disabled style='background-color:" + estadoPosiciones[i] + "' type='color' value='" + intento[i] + "'>"

    resumenTurnoActual += '</div><br><div><i>Resultado</i><br><i>' + calcula_resultado(intento, secreto) + '</i></div>'

    return resumenTurnoActual
