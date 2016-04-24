import requests
from django.db import models
from datetime import datetime as datetime_
import datetime
import time

# Create your models here.

WEATHER_APP_ID = '9b48f2acc414d715d89ad001a3456650'
WEATHER_API = 'http://api.openweathermap.org/data/2.5/group?id=%s&units=metric&appid=%s'


def home(request):
    msg = {'header': 'loh', 'main_text': 'pidor'}
    if request.user.is_authenticated():
        msg['header'] = ', '.join(['Your homepage', request.user.username])
        msg['main_text'] = 'Weather info will be here :)'
    else:
        msg['header'] = 'You can\'t see this page :('
        msg['main_text'] = 'Pleese login to see this page.'
    return msg


def update_info():
    all_id = ','.join(map(lambda x: str(x.id), City.objects.all()))
    general_info = requests.get(WEATHER_API % (all_id, WEATHER_APP_ID)).json()
    # print(general_info)
    for i in range(general_info['cnt']):
        info = general_info['list'][i]
        # print(info)
        city = City.objects.get(id=info['id'])
        time_ = datetime_.fromtimestamp(info['dt']).replace(tzinfo=None)
        temperature = info['main']['temp']
        wind_speed = info['wind']['speed']
        try:
            rain = float(info['rain']['1h'])
        except:
            rain = 0
        try:
            snow = float(info['snow']['1h'])
        except:
            snow = 0
        try:
            clouds = float(info['clouds']['all'])
        except:
            clouds = 0
        weather_info = WeatherInfo(
            city=city,
            time=time_,
            temperature=temperature,
            wind_speed=wind_speed,
            rain=rain,
            snow=snow,
            clouds=clouds
        )
        weather_info.save()

class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


def set_pk_for_weather_city(time_, city):
    return int(
            (time_.replace(tzinfo=None) - datetime_(2016, 1, 1).
             replace(tzinfo=None)).total_seconds() // 60 * 10 + city
    )


class WeatherInfo(models.Model):
    city = models.ForeignKey(City)
    time = models.DateTimeField()
    temperature = models.FloatField()
    rain = models.FloatField()
    snow = models.FloatField()
    clouds = models.FloatField()
    wind_speed = models.FloatField()

    def __str__(self):
        return ', '.join([self.time.strftime("%d %m %y %H:%M:%S"), str(self.temperature) + 'K', str(self.wind_speed) + 'mps'])