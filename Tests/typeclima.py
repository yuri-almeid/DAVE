import requests
'''
{ Lyon FR Exemplo
'wind': {'speed': 1.5}, 'id': 2996944, 'coord': {'lat': 45.76, 'lon': 4.83},
'weather': [{'icon': '04n', 'main': 'Clouds', 'id': 804, 'description': 'overcast clouds'}],
'cod': 200, 'base': 'stations',
'main': {'temp_min': 279.15, 'pressure': 1018, 'temp_max': 281.15, 'humidity': 100, 'temp': 280.39},
'visibility': 10000, 'name': 'Lyon',
'sys': {'message': 0.004, 'type': 1, 'id': 5576, 'sunset': 1516638731, 'sunrise': 1516605168, 'country': 'FR'},
'clouds': {'all': 90}, 'dt': 1516586400}
'''
'''
def get_wea(city):
    api_ad = 'http://api.openweathermap.org/data/2.5/weather?q='
    wea_id = '&appid=b0480a6aefadfc26883d724d5c571229'
    url = api_ad + city + wea_id
    json_data = requests.get(url).json()
    ss = json_data['weather'][0]['description']
    return ss
while True:
    try:
        city = input('City name: ')
        x = get_wea(city)
        print(x)
    except:
        print('not finded')

'''
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
    # Converte as temperaturas para celcius em valores inteiros aproximados
    temp = int(temper - 273)
    temp_min = int(Min - 273)
    temp_max = int(Max - 273)

    return desc, temp, temp_min, temp_max, main

while True:
    try:
        city = input('City name: ')
        x = get_weather(city)
        print(x)
    except:
        print('not finded')
