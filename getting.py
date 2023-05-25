import requests

s_city = "Moscow,RU"
appid = "d12d61862fbf820144493cf479c73e79"

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': s_city, 'units': 'metric',
                           'lang': 'ru', 'APPID': appid})
data = res.json()

print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nСкорость ветра <", i['wind']['speed'],
          "> \r\nВидимость <", i['visibility'], ">")
    print("____________________________")
