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
def k_to_c(temp):
    temper = temp - 273
    return temper
def get_wea(city):
    api_ad = 'http://api.openweathermap.org/data/2.5/weather?q='
    wea_id = '&appid=b0480a6aefadfc26883d724d5c571229'
    url = api_ad + city + wea_id

    json_data = requests.get(url).json()
    desc = json_data['weather'][0]['description']
    ss = json_data['weather'][0]['main']
    main = json_data['main']['temp']
    Min = json_data['main']['temp_min']
    Max = json_data['main']['temp_max']
    temp = k_to_c(main)
    temp_max = k_to_c(Max)
    temp_min = k_to_c(Min)
    print(json_data)
    return desc, temp, temp_max, temp_min, ss


city = input('City name: ')
#city = 'Vitória da conquista'
x = get_wea(city)
print(x)



