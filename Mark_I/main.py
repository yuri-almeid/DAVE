#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#   D.A.V.E. - Digital Asssistant Virtually Emulated
#   Mark I
#   Language: English
#   Author: Yuri L. Almeida
#

'''----------------------------------------------------------------------------'''
# Importando Módulos
from chatterbot.trainers import ListTrainer # módulo treinador
from chatterbot import ChatBot # módulo do ChatBot
from datetime import datetime # módulo de tempo
from datetime import date # Módulo de tempo (preciso)
import os # módulo do sistema operacional
import time # módulo temporizador
import wikipedia # módulo do Wikipédia
import wolframalpha # Mdulo do wolfram Alpha
import webbrowser # Módulo do browser
import psutil # Módulo de utilidades do sistema
import random # Módulo de resposta dandômica


'''----------------------------------------------------------------------------'''
## Cria ChatBot *Comentar caso ja tenha treinado
#bot = ChatBot('DAVE')          
## Inicia chatbot sem treinar *Descomentar caso tenha sido treinado
bot = ChatBot('DAVE', read_only = True)


'''----------------------------------------------------------------------------'''
## Definições
bot.set_trainer(ListTrainer)  # Define treinamento
wikipedia.set_lang('en') # Define lingua da pesquisa pelo wikipedia


'''----------------------------------------------------------------------------'''
## Palavras Chave

keywords_def = ['what is', 'who was', 'who is', 'definition of', 'define'] # busca de definição

keywords_search = ['search for', 'look in the internet for', 'search in the internet for',
                   'seach about', 'search in the internet about',
                   'look in the internet about'] # Pesquisa na internet


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
## Função para executar comandos
def run_cmd(cmd_type):
    result = None
    # Comando de horas
    if cmd_type == 'asktime':
        now = datetime.now()
        result = 'It is ' + str(now.hour) + ' hours and ' + str(now.minute) + ' minutes.'

    # Comando de data
    elif cmd_type == 'askdate':
        #now = datetime.now()
        now = date.today()
        #months = ['January','February','March','April','May','June','July','August',
        #          'September','October','November','December']
        #result = 'Today is ' + months[now.month - 1] + ' ' + str(now.day) + '.'
        result = str(now.strftime("Today is %B %d, it's a %A")) + '.'
        

    # Comando de temperatura do CPU
    elif cmd_type == 'askcputemp':
        res = os.popen('vcgencmd measure_temp').readline()
        CPU = res.replace("temp=", '').replace("'C\n",'')
        result = 'The system is operating at ' + str(CPU) + ' degrees Celcius.'

    # Comando de fechar programa
    elif cmd_type == 'askexit':
        print('D.A.V.E.: Program finished!')
        exit()

    # Comando de jogar uma moeda
    elif cmd_type == 'askcoin':
        resp = random.choice(['heads','tails'])
        result = 'You got ' + str(resp) + '.'
        
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
        result = wikipedia.summary(results[0], sentences = 2)

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
# Convesa sem Reconhecimento de voz
''' '''
print('---------------------------------------')
print('D.A.V.E.: Hello Sir, How can I help you today?')
while True:
    quest = input('You: ')
    quest = quest.lower() # Passa tudo pra minúsculo

    resp = run_cmd(evaluate(quest)) # Verifica qual o tipo de comando

    if resp == None:
        resp = get_wiki(quest) # Chama função wikipedia
        if resp == None:
            resp = bot.get_response(quest) # chatbot resposta

    print('D.A.V.E.: ' + str(resp)) # Concatena resposta ao chat
    #print('Tipo de comando: ',evaluate(quest)) # mostra o tipo de comando
''' '''



