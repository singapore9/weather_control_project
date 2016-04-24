import requests
from django.db import models
from datetime import datetime as datetime_
import datetime
import time

# Create your models here.

WEATHER_APP_ID = '9b48f2acc414d715d89ad001a3456650'
WEATHER_API = 'http://api.openweathermap.org/data/2.5/forecast/city?id=%s&APPID=%s'


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
    # general_info = requests.get(WEATHER_API % ())
    print(all_id)

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
    temperature = models.IntegerField()
    rain = models.IntegerField()
    snow = models.IntegerField()
    clouds = models.IntegerField()
    wind_speed = models.FloatField()