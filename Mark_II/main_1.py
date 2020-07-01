#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#   D.A.V.E. - Digital Asssistant Virtually Emulated
#   Mark II
#   Language: English
#   Author: Yuri L. Almeida
#

'''----------------------------------------------------------------------------'''
# Importando Módulos
from sendmailmode import Send_Mail, Send_Note # Função criada para mandar email
from chatterbot.trainers import ListTrainer # módulo treinador
from chatterbot import ChatBot # módulo do ChatBot
from datetime import datetime # módulo de tempo
from datetime import date # Módulo de tempo (data)
from calcmode import calc_mode # Função criada para modo matemático
import speech_recognition as sr # Módulo de reconhecimento de fala
import RPi.GPIO as gpio # Módulo dos pinos GPIO do Raspberry pi
import pyttsx3 # Módulo sintetizador de voz
import os # módulo do sistema operacional
import time # módulo temporizador
import wikipedia # módulo do Wikipédia
import wolframalpha # Mdulo do wolfram Alpha
import webbrowser # Módulo do browser
import psutil # Módulo de utilidades do sistema
import random # Módulo de resposta dandômica
import requests # Módulo para requerimento web


'''----------------------------------------------------------------------------'''
## Cria engine para sintetizar a voz
engine = pyttsx3.init()

'''
voices = engine.getProperty('voices')
for voice in voices:
    # Define idioma do sintetizador
    if voice.name == 'english':
        engine.setProperty('voice', voice.id)
'''


'''----------------------------------------------------------------------------'''
## Cria ChatBot *Comentar caso ja tenha treinado
#bot = ChatBot('DAVE')          
## Inicia chatbot sem treinar *Descomentar caso tenha sido treinado
bot = ChatBot('DAVE', read_only = True)


'''----------------------------------------------------------------------------'''
## Função para definições dos pinos GPIO
def set_gpio():
    gpio.setmode(gpio.BOARD) # Define tipo de pinagem
    gpio.setup(11, gpio.OUT) # Seta pino 11 como saída
    gpio.setup(12, gpio.OUT) # Seta pino 12 como saída
    gpio.setup(13, gpio.OUT) # Seta pino 11 como saída
    gpio.setup(15, gpio.OUT) # Seta pino 12 como saída
    gpio.setup(16, gpio.OUT) # Seta pino 11 como saída


'''----------------------------------------------------------------------------'''
## Definições
bot.set_trainer(ListTrainer)  # Define treinamento
wikipedia.set_lang('en') # Define lingua da pesquisa pelo wikipedia
set_gpio() # Difinições do uso dos pinos GPIO


'''----------------------------------------------------------------------------'''
## Palavras Chave

keywords_def = ['what is', 'who was', 'who is', 'definition of', 'define',
                'what do you know about', "who's"] # busca de definição

keywords_search = ['search for', 'look in the internet for', 'search in the internet for',
                   'seach about', 'search in the internet about',
                   'look in the internet about'] # Pesquisa na internet

keywords_weather = ["how's the weather in", "how is the weather in",
                    "how it's going the weather in", "how's the temperature in",
                    "how is the temperature in"] # Pesquisa por temperatura


'''----------------------------------------------------------------------------'''
## Criando dicionário global para comandos
dict_cmds = {}
def load_cmds(): # Função que lê todos os comandos
    lines = open('cmd.txt', 'r').readlines()
    for line in lines:
        line = line.replace('\n', '')
        parts = line.split('\t') # Separa comando do tipo de comando
        dict_cmds.update({ parts[0] : parts[1]})


'''----------------------------------------------------------------------------'''
## Treinando o ChatBot
## Treinamento deve ser feito apenas uma vez
''' 
for _file in os.listdir('database'):                   # Passa por todo o arquivo
    lines = open('database/' + _file, 'r').readlines() # Abre em leitura e lê linhas
    bot.train(lines)
''' 


'''----------------------------------------------------------------------------'''
## Passando Comandos

def evaluate(text):
    result = None
    try:
        result = dict_cmds[text]
    except:
        result = None
    return result


'''----------------------------------------------------------------------------'''
## Função para voz
def say(text):
    #engine.setProperty('rate', 180) # Define velocidade
    engine.say(text)
    engine.runAndWait()

    return None


'''----------------------------------------------------------------------------'''
## Funções para operar pinos GPIO

def pin_on(pin): # Função que liga
    gpio.output(pin, gpio.HIGH)
    
def pin_off(pin): # Função que desliga
    gpio.output(pin, gpio.LOW)


'''----------------------------------------------------------------------------'''
## Função temperatura
def get_weather(city):
    weather_ad = 'http://api.openweathermap.org/data/2.5/weather?q=' 
    weather_id = '&appid=b0480a6aefadfc26883d724d5c571229'
    weather_URL = weather_ad + city + weather_id # URL do requerimento online
    weather_data = requests.get(weather_URL).json() # Requere o url em arquivo JSON
    # Pega variveis do arquivo JSON
    desc = weather_data['weather'][0]['description'] 
    temper = weather_data['main']['temp']
    Min = weather_data['main']['temp_min']
    Max = weather_data['main']['temp_max']
    main = weather_data['weather'][0]['main']
    # Converte as temperaturas para celsius em valores inteiros aproximados
    temp = int(temper - 273)
    temp_min = int(Min - 273)
    temp_max = int(Max - 273)

    return desc, temp, temp_min, temp_max, main


'''----------------------------------------------------------------------------'''
## Função para executar comandos
def run_cmd(cmd_type):
    result = None

    # 0 Comando para testes no programa
    if cmd_type == 'asktest':

        result = None
        
    # 1 Comando de horas
    elif cmd_type == 'asktime':
        now = datetime.now()
        result = 'It is ' + str(now.hour) + ' hours and ' + str(now.minute) + ' minutes.'
        
    # 2 Comando de data
    elif cmd_type == 'askdate':
        now = date.today()
        result = str(now.strftime("Today is %B, %d, it's a %A")) + '.'
        
    # 3 Comando de temperatura do CPU
    elif cmd_type == 'askcputemp':
        res = os.popen('vcgencmd measure_temp').readline()
        CPU = res.replace("temp=", '').replace("'C\n",'')
        say('Okay sir!')
        say('Analizing system.')
        time.sleep(1)
        result = 'The system is operating at ' + str(CPU) + ' degrees Celcius.'
        
    # 4 Comando de fechar programa
    elif cmd_type == 'askexit':
        say('Okay sir!')
        gpio.cleanup() # Desfaz modificações nos pinos GPIO
        say('All the Systems are closed!')
        print('D.A.V.E.: All the Systems are closed!')
        exit()
        
    # 5 Comando que lista comandos
    elif cmd_type == 'askcommandlist':
        say('Yes sir!')
        print()
        print()
        print('-- COMMAND LIST --')
        for k, v in dict_cmds.items(): # Lista comando
            print(v,' => ',k)
        result = 'All the commands was listed at the shell!'
        
    # 6 Comando de responde nome do usuário
    elif cmd_type == 'askname':
        file = open('username.txt', 'r')
        username = file.read()
        file.close()
        result = 'Your name is ' + username + '.'
        
    # 7 Comando de jogar uma moeda
    elif cmd_type == 'askcoin':
        resp = random.choice(['heads','tails'])
        result = 'You got ' + str(resp) + '.'
        
    # 8 Comando para modo matemático
    elif cmd_type == 'askcalcmode':
        say('Yes sir!')
        say('Calculation mode inicialized!')
        say('Please, say your operation!')
        print('D.A.V.E.: Please, say your operation: ')
        mathop = input('You: ')
        result = str(calc_mode(mathop))
        
    # 9 Comando EE de conscincia
    elif cmd_type == 'askselfcons':
        print("D.A.V.E.: That's a good question")
        say("That's an good question")
        result = "Can you prove yours?"
        
    # 10 Comando de bom dia
    elif cmd_type == 'askgmorning':
        now = date.today() # Coleta dados da data
        # Busca cidade cadastrada
        file = open('homecity.txt', 'r')
        homecity = file.read()
        file.close()
        
        print("D.A.V.E.: Good morning, Sir!")
        say("Good morning, Sir!")
        aboutday = str(now.strftime("Today is %B, %d, it's a %A"))
        print('D.A.V.E.: ' + aboutday)
        say(aboutday)
        # Coleta dados do clima na cidade cadastrada
        waether_data = get_weather(homecity)
        description = waether_data[0]
        temperature = waether_data[1]
        weather_type = waether_data[4]
        abouttemp = "The temperature looks about " + str(temperature) + " degrees"
        print("D.A.V.E.: " + abouttemp)
        say(abouttemp)
        
        # verifica o estado da temperatura e assim:
        if weather_type == 'Rain' or weather_type == 'Thunderstorm':
            print("D.A.V.E.: And you should take an umbrella.")
            say('And you should take an umbrella.')
            result = "Because today there will be a " + description + '.'
        else:
            result = "Have a nice day with " + description + ' today.'
            
    # 11 Comando de clima
    elif cmd_type == 'askweatherlocal':
        # Verifica local cadastrado
        print("D.A.V.E.: Wait a minute.")
        say('Wait a minute!')
        file = open('homecity.txt', 'r')
        homecity = file.read()
        file.close()
        # Pesquisa clima no local cadastrado
        waether_data = get_weather(homecity)
        description = waether_data[0]
        temperature = waether_data[1]
        #temp_min =  waether_data[2]
        #temp_max =  waether_data[3]
        weather_type = waether_data[4]
        
        # Execução do comando
        abouttemp = "The temperature looks about " + str(temperature) + " degrees"
        print("D.A.V.E.: " + abouttemp)
        say(abouttemp)
        print("D.A.V.E.: Today there will be a " + description + '.' )
        say("Today there will be a " + description + '.' )
        
        # verifica o estado da temperatura e assim:
        if weather_type == 'Rain' or weather_type == 'Thunderstorm':
            add = 'An umbrella is a good company for today.'
        else:
            add = ' '

        result = add
        
    # 12 Comando do guarda chuva
    elif cmd_type == 'askumbrella':
        # Verifica local cadastrado
        file = open('homecity.txt', 'r')
        homecity = file.read()
        file.close()
        # Pesquisa clima no local cadastrado
        waether_data = get_weather(homecity)
        description = waether_data[0]
        weather_type = waether_data[4]
        # Verifica condição climatica
        if weather_type == 'Rain' or weather_type == 'Thunderstorm':
            ans = 'An umbrella is a good company for today.'
        else:
            ans = "No, won't rain, "

        result = ans + "today there will be a" + description + '.'
        
    # 13 Comando EE do criador
    elif cmd_type == 'askcreator':
        result = 'My creator was, Yuri Almeida'
        
    # 14 Comando de repetição
    elif cmd_type == 'askrepetition':
        print("D.A.V.E.: Okay, Sir!")
        say('Okay, Sir!')
        print("D.A.V.E.: Tell me what I should repeat.")
        say('Tell me what i should repeat.')
        repetition = input('You: ')
        time.sleep(0.3)
        result = repetition

    # 15 Comando EE sobre o assistente
    elif cmd_type == 'askaboutme':
        print("D.A.V.E.: My name is DAVE")
        say('My name is Dave')
        print("D.A.V.E.: And DAVE means")
        say('and Dave means.')
        print("D.A.V.E.: Digital Asssistant Virtually Emulated")
        say('Digital Asssistant Virtually Emulated.')
        print("D.A.V.E.: I was inveted by Yuri L. Almeida")
        say('I was inveted by, Yuri L. Almeida')
        print("D.A.V.E.: In January 08 of 2018 my first version was 'alive'")
        say('In January 08 of 2018 my first version was, alive')
        print("D.A.V.E.: And now, I can do a lot of things")
        say('And now, I can do a lot of things')
        print("D.A.V.E.: Ask me about the weather or date")
        say('Ask me about the weather or date')

        result = 'Or try ask me about something else.'

    # 16 Comando Pedra, papel e tesoura
    elif cmd_type == 'askplayrps':
        print("D.A.V.E.: Okay, let's play!")
        say("Okay... let's play!")
        print("D.A.V.E.: 3")
        say("3")
        time.sleep(0.3)
        print("D.A.V.E.: 2")
        say("2")
        time.sleep(0.3)
        print("D.A.V.E.: 1")
        say("1")
        time.sleep(0.3)
        resp = random.choice(['Rock','Paper','Scissors'])

        result = str(resp)

    # 17 Comando para mandar email
    elif cmd_type == 'asksendmail':
        print("D.A.V.E.: Okay")
        say("Okay")
        print("D.A.V.E.: Would you like speak the mail, or would you like to type it?")
        say("Would you like speak the mail?")
        say("Or Would you like to type it?")
        cs = input('You: ')
        
        if cs == 'type':
            print("D.A.V.E.: Okay, please, type the mail.")
            say("Okay, please, type the mail.")
            mail = input('You: ')
        elif cs == 'say' or cs == 'speak' or cs == 'speech':
            print("D.A.V.E.: Okay, please, say the mail.")
            say("Okay, please, say the mail.")
            mail = input('You: ')
        else:
            return "Sorry, but you said something wrong."
        
        print("D.A.V.E.: Now enter at the shell the email of the person you are sending the message to.")
        say("Now enter, at the shell the email")
        say("of the person you are sending the message to")
        mailadrs = input('You: ')
        print("D.A.V.E.: Wait some seconds while I send this email.")
        say("Wait some seconds while I send this email.")

        ans = Send_Mail(mail, mailadrs)
        result = ans

    # 18 Comando para lembretes no email
    elif cmd_type == 'asknote':
        print("D.A.V.E.: Yes!")
        say("Yes!")
        print("D.A.V.E.: Would you like speak the note, or would you like to type it?")
        say("Would you like speak the note?")
        say("Or Would you like to type it?")
        
        cs = input('You: ')
        if cs == 'type' or cs == 'type the note':
            print("D.A.V.E.: Okay, please, type the note.")
            say("Okay, please, type the note.")
            note = input('You: ')
        elif cs == 'say' or cs == 'speak' or cs == 'speech' or cs == 'speak the note':
            print("D.A.V.E.: Okay, please, say the note.")
            say("Okay, please, say the note.")
            note = input('You: ')
        else:
            return "Sorry, but you said something wrong."

        print("D.A.V.E.: Wait some seconds while I send you your note as a email.")
        say("Wait some seconds while I send you")
        say("your note as a email.")

        ans = Send_Note(note)
        result = ans

    # 19 Comando de Timer
    elif cmd_type == 'asktimer':
        print("D.A.V.E.: Okay")
        say("Okay")
        print("D.A.V.E.: Just say the time.")
        say("Just say the time.")
        Time = input('You: ')
        Time = Time.split(' ')
        if Time[-1] == 'minute' or Time[-1] == 'minutes':
            print("D.A.V.E.: Timer inicialized!")
            say("Timer inicialized!")
            minutes = Time[0]
            wait = int(minutes)*60
            time.sleep(wait)
            result =  "The timer is over Sir"
        elif Time[-1] == 'second' or Time[-1] == 'seconds':
            print("D.A.V.E.: Timer inicialized!")
            say("Timer inicialized!")
            wait = Time[0]
            wait = int(wait)
            time.sleep(wait)
            result =  "The timer is over Sir"
        elif Time[-1] == 'hour' or Time[-1] == 'hours':
            result = 'This time is very long, you should set an alarm'
        else:
            result = "I couldn't understand what you said."

    # 20 Comando de luz para ligar sala
    elif cmd_type == 'asklivingroomon':
        resp = random.choice(['Okay','Yes Sir','Yes'])
        print('D.A.V.E.: ' + resp)
        say(resp)
        pin_on(13) # Chama função que aciona o gpio do pino 13
        result = ' '
        
    # 21 Comando de luz para desligar sala
    elif cmd_type == 'asklivingroomoff':
        resp = random.choice(['Okay','Yes Sir','Yes'])
        print('D.A.V.E.: ' + resp)
        say(resp)
        pin_off(13) # Chama função que aciona o gpio do pino 13
        result = ' '

    # 22 Comando de luz para ligar quarto
    elif cmd_type == 'askbedroomon':
        resp = random.choice(['Okay','Yes Sir','Yes'])
        print('D.A.V.E.: ' + resp)
        say(resp)
        pin_on(11) # Chama função que aciona o gpio do pino 11
        result = ' '

    # 23 Comando de luz para desligar quarto
    elif cmd_type == 'askbedroomoff':
        resp = random.choice(['Okay','Yes Sir','Yes'])
        print('D.A.V.E.: ' + resp)
        say(resp)
        pin_off(11) # Chama função que aciona o gpio do pino 11
        result = ' '

    # 24 Comando de luz para ligar cozinha
    elif cmd_type == 'askkitchenon':
        resp = random.choice(['Okay','Yes Sir','Yes'])
        print('D.A.V.E.: ' + resp)
        say(resp)
        pin_on(16) # Chama função que aciona o gpio do pino 16
        result = ' '

    # 25 Comando de luz para desligar cozinha
    elif cmd_type == 'askkitchenoff':
        resp = random.choice(['Okay','Yes Sir','Yes'])
        print('D.A.V.E.: ' + resp)
        say(resp)
        pin_off(16) # Chama função que aciona o gpio do pino 16
        result = ' '

    # 26 Comando de luz para ligar corredor
    elif cmd_type == 'askhallon':
        resp = random.choice(['Okay','Yes Sir','Yes'])
        print('D.A.V.E.: ' + resp)
        say(resp)
        pin_on(15) # Chama função que aciona o gpio do pino 15
        result = ' '

    # 27 Comando de luz para desligar corredor
    elif cmd_type == 'askhalloff':
        resp = random.choice(['Okay','Yes Sir','Yes'])
        print('D.A.V.E.: ' + resp)
        say(resp)
        pin_off(15) # Chama função que aciona o gpio do pino 15
        result = ' '

    # 28 Comando de luz para ligar varanda
    elif cmd_type == 'askoutsideon':
        resp = random.choice(['Okay','Yes Sir','Yes'])
        print('D.A.V.E.: ' + resp)
        say(resp)
        pin_on(12) # Chama função que aciona o gpio do pino 12
        result = ' '

    # 29 Comando de luz para desligar varanda
    elif cmd_type == 'askoutsideoff':
        resp = random.choice(['Okay','Yes Sir','Yes'])
        print('D.A.V.E.: ' + resp)
        say(resp)
        pin_off(12) # Chama função que aciona o gpio do pino 12
        result = ' '

    # 30 Comando que desliga todas as luzes
    elif cmd_type == 'askalllightsoff':
        resp = random.choice(['Okay','Yes Sir','Yes'])
        print('D.A.V.E.: ' + resp)
        say(resp)
        pin_off(11)
        pin_off(12)
        pin_off(13)
        pin_off(15)
        pin_off(16)
        result = ' '

    # 31 Comando que liga todas as luzes
    elif cmd_type == 'askalllightson':
        resp = random.choice(['Okay','Yes Sir','Yes'])
        print('D.A.V.E.: ' + resp)
        say(resp)
        pin_on(11)
        pin_on(12)
        pin_on(13)
        pin_on(15)
        pin_on(16)
        result = ' '
        
    else:
        result = None
    return result


'''----------------------------------------------------------------------------'''
## Função de pesquisa no Wikipedia

def get_wiki(text):
    result = None
    results = None
    # Pesquisa se estiver com palavra chave
    if text is not None:
        for key in keywords_def:
            if text.startswith(key):
                result = text.replace(key, '')

    if result is not None:
        results = wikipedia.search(result)
        ans = wikipedia.summary(results[0], sentences = 2)
        # Solução para bug da fala
        print('D.A.V.E.: ' + ans)
        ans = ans.split(', ')
        for phrase in ans:
            say(phrase)
        result = ' '

    return result


'''----------------------------------------------------------------------------'''
## Função do wlfram de conhecimento computacional

def Comp_Knowledge(text):
    # Cadastro do cliente
    app_id = "5H3AXG-4PHL3HT6YJ"
    client = wolframalpha.Client(app_id)
    # Obtendo resposta
    question = str(text)
    
    try: # Caso tenha resposta
        answer = client.query(question)
        ans = next(answer.results).text
        if ans == '(data not available)':
            result = None
        else:
            # Solução para bug da fala
            print('D.A.V.E.: ' + ans)
            ans = ans.split('\n')
            for phrase in ans:
                say(phrase)
            result = ' '      
    except: # Caso não tenha resposta
        result = None

    return result


'''----------------------------------------------------------------------------'''
## Função de pesquisa na internet
## *Falta Biblioteca do google
'''
def search_web(text):
    result = None

    if text is not None:
        for key in keywords_search:
            if text.startswith(key):
                result = text.replace(key, '')

        if result is not None:
            for url in search(text, stop = 3):
                webbrowser.open_new_tab(url)
                break
            return 'Pesquisando por ' + result.rstrip()
    return result
'''     


'''----------------------------------------------------------------------------'''
# Lista de comandos catalogados

load_cmds() # Carrega comandos
'''
for k, v in dict_cmds.items(): # Lista comando antes do programa começar
    print(k,' > ',v)
'''

'''----------------------------------------------------------------------------'''

# Programa principal
''' '''
say('Hello Sir!')
os.system('clear')
print('============================== D.A.V.E. ==============================')
print('D.A.V.E.: Hello Sir!')
print('D.A.V.E.: All the systems are operanting!')
say('All the systems are operanting') 
while True:
    conf = 1
    quest = input('You: ')
    quest = quest.lower() # Passa tudo pra minúsculo

    resp = run_cmd(evaluate(quest)) # Verifica qual o tipo de comando

    if resp == None:
        resp = Comp_Knowledge(quest) # Chama função de conhecimento computacional
        if resp == None:
            resp = get_wiki(quest) # Chama função wikipedia
            if resp == None:
                resp = bot.get_response(quest) # chatbot resposta
                conf = float(resp.confidence) # Checa confiança na resposta


    if conf > 0.5:
        if resp != ' ':
            print('D.A.V.E.: ' + str(resp)) # Concatena resposta ao chat
            say(str(resp))
            #print('Tipo de comando: ',evaluate(quest)) # mostra o tipo de comando
    else:
        print("D.A.V.E.: Sir, I'm not sure how to answer this!") # Concatena resposta ao chat
        say("Sir, I'm not sure how to answer this!")
        
''' '''



