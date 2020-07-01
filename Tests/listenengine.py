import speech_recognition as sr

r = sr.Recognizer()

def rec():
    with sr.Microphone() as source:
        print('Say something: ')
        audio = r.listen(source)
        print('done!')
    try:
        tt = r.recognize_google(audio)
        print('You said: ' + tt)
    except Exception as e:
        print(e)

while True:
    rec()
