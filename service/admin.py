from django.contrib import admin
from . import models


@admin.register(models.Pancard)
class PancardAdmin(admin.ModelAdmin):
    list_display = ['number', 'user', 'confidence', 'result', 'status']


@admin.register(models.PancardImage)
class PancardImageAdmin(admin.ModelAdmin):
    list_display = ['pancard', 'image']


@admin.register(models.PanOriginal)
class PanOriginalAdmin(admin.ModelAdmin):
    list_display = ['image']

