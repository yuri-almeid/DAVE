from urllib.request import urlopen
import json



 
data = urlopen('http://api.openweathermap.org/data/2.5/weather?q=Itajai,BR&units=metric&lang=pt')
html = data.read()
weather = json.loads(html)
temperatura = str(weather['main']['temp']) + ' graus'
nebulosidade = str(weather['clouds']['all']) + ' %'
umidade = str(weather['main']['humidity']) + ' %'
print(temperatura)
print(nebulosidade)
print(umidade)
