import speech_recognition as sr
import pyaudio
import pyttsx3

engine = pyttsx3.init("sapi5")
recognizer = sr.Recognizer()

with sr.Microphone() as source:
  while True:
    rec = recognizer.listen(source)
    aux = recognizer.recognize_google(rec)

    print('User: ' + str(aux))

    print('Bot: ' + str(aux))
    engine.say(aux)
    engine.runAndWait()
