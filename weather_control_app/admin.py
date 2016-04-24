from django.contrib import admin
from weather_control_app import models


class AdminWeatherInline(admin.TabularInline):
    model = models.WeatherInfo
    readonly_fields = ['time', 'temperature', 'rain', 'snow', 'clouds', 'wind_speed']
    extra = 0


class AdminCity(admin.ModelAdmin):
    fields = ['name', 'id']
    inlines = [AdminWeatherInline]

admin.site.register(models.City, AdminCity)