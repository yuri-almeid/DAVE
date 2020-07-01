from datetime import datetime
from datetime import date

import pyttsx3 # Módulo sintetizador de voz

engine = pyttsx3.init()

dict_alarms = {}

def load_cmds(): # Função que lê todos os alarmes
    dict_alarms = {}
    lines = open('alarms.txt', 'r').readlines()
    for line in lines:
        line = line.replace('\n', '')
        parts = line.split('\t') # Separa descricao da hora
        dict_cmds.update({ parts[0] : parts[1]})

## Função para voz
def say(text):
    #engine.setProperty('rate', 180) # Define velocidade
    engine.say(text)
    engine.runAndWait()

    return None

say('the Alarms are operating.')

now = datetime.now()
current_hour = str(now.hour) + ':' + str(now.minute)
