from django.contrib import admin
from weather_control_app import models


class AdminCity(admin.ModelAdmin):
    fields = ['name', 'id']

admin.site.register(models.City, AdminCity)