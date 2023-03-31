from django_admin_geomap import ModelAdmin
from .models import RemarkablePlaces, Weather
from django.contrib import admin
from import_export.admin import ExportActionMixin


@admin.register(RemarkablePlaces)
class RemarkablePlacesAdmin(ModelAdmin):
    """Админка для примечательный мест"""
    list_display = ('name', 'lon', 'lat', 'rating')

    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"


@admin.register(Weather)
class WeatherAdmin(ExportActionMixin, admin.ModelAdmin):
    """Админка для сводок погоды"""
    list_display = ('remarkable_place', 'date_time', 'temp_c', 'humidity', 'pressure_mb', 'wind_dir', 'wind_kph',)
    search_fields = ['date_time', 'remarkable_place__name']
    list_filter = ['date_time', 'remarkable_place__name']
    readonly_fields = ('remarkable_place', 'date_time', 'temp_c', 'humidity', 'pressure_mb', 'wind_dir', 'wind_kph',)

