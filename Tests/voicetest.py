'''
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    #print(voice.name)
    if voice.name == 'english':
        engine.setProperty('voice', voice.id)
while True:
    sayit = input('Say it: ')
    sayit = str(sayit)
    engine.say(sayit)
    engine.runAndWait()
'''
'''
default
english
en-scottish
english-north
english_rp
english_wmids
english-us
en-westindies
french
brazil
portugal
'''

import pyttsx3
en = pyttsx3.init()

def say(text):
    en.say(text)
    en.runAndWait()
    return None
while True:
    sayit = input('Say it: ')
    sayit = str(sayit)
    say(sayit)

