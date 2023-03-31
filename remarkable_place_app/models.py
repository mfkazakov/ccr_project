from django.db import models
from django_admin_geomap import GeoItem
import django.utils.timezone


class RemarkablePlaces(models.Model, GeoItem):
    name = models.CharField(max_length=255, null=False, verbose_name='Название места')
    lon = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    rating = models.IntegerField(null=False, blank=False, verbose_name='Рейтинг')

    def __str__(self):
        return self.name

    @property
    def geomap_longitude(self):
        return '' if self.lon is None else str(self.lon)

    @property
    def geomap_latitude(self):
        return '' if self.lat is None else str(self.lat)

    class Meta:
        verbose_name = 'Примечательное место'
        verbose_name_plural = 'Примечательные места'


class Weather(models.Model):
    temp_c = models.CharField(max_length=50, verbose_name='Температура')
    humidity = models.CharField(max_length=50, verbose_name='Влажность')
    pressure_mb = models.CharField(max_length=50, verbose_name='Давление')
    wind_dir = models.CharField(max_length=50, verbose_name='Направление ветра')
    wind_kph = models.CharField(max_length=50, verbose_name='Скорость ветра')
    date_time = models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время измерений')

    remarkable_place = models.ForeignKey(RemarkablePlaces, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сводка погоды'
        verbose_name_plural = 'Сводка погоды'

