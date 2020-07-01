import pyttsx3
import os

engine = pyttsx3.init()
'''
rate = engine.getProperty('rate')
voice = engine.getProperty('voice')
volume = engine.getProperty('volume')
print(rate)
print(voice)
print(volume)
'''
engine.setProperty('rate', 140)

engine.runAndWait()




'''
newrate = 50
while newrate <= 300:
    engine.setProperty('rate', newrate)
    engine.say('Testing different voice rates.')
    engine.runAndWait()
    newrate = newrate + 50

engine.setProperty('rate', 125)

newvol = 0.1
while newvol <= 1:
    engine.setProperty('volume', newvol)
    engine.say('Testing different voice volumes.')
    engine.runAndWait()
    newvol = newvol + 0.3
'''
