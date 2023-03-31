from celery import shared_task
from .models import RemarkablePlaces, Weather
import requests


@shared_task()
def get_weather():
    """Получение текущей погоды в примечательных местах"""
    places = RemarkablePlaces.objects.all()
    with requests.session() as session: # переделать на ассинхр
        for place in places:
            url = f'http://api.weatherapi.com/v1/current.json?key=0a6586359d6e4c3084c73940232802&q={str(place.lon)},{str(place.lat)}&aqi=no'
            with session.get(url) as res:
                try:
                    data = res.json()
                except Exception as e:
                    print(str(e))   # тут должно быть логгирование
                    return
                try:
                    Weather(
                        temp_c=data['current']['temp_c'],
                        humidity=data['current']['humidity'],
                        pressure_mb=data['current']['pressure_mb'],
                        wind_dir=data['current']['wind_dir'],
                        wind_kph=data['current']['wind_kph'],

                        remarkable_place=place,
                    ).save()
                except Exception as e:
                    print(str(e))   # тут должно быть логгирование
                    return

