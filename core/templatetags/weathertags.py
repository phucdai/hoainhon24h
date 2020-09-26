import requests
from django import template

register = template.Library()

@register.simple_tag
def Weather():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Quy nhon&appid=c15b2c26b7d5d0028868fb0d2de8a80c')
    reponsedata = r.json()
    main = reponsedata['main']
    temp = main['temp'] - 273
    temp_max = main['temp_max'] - 273
    temp_min = main['temp_min'] - 273
    city = reponsedata['name']
    weather = reponsedata['weather'][0]
    icon = weather['icon']
    data = {
        'temp': temp,
        'temp_max': int(temp_max),
        'temp_min': int(temp_min),
        'city': city,
        'icon': icon,
    }
    return data