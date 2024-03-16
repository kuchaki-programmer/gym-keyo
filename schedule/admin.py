from django.contrib import admin
from . import models

admin.site.register(models.WeekDay)
admin.site.register(models.HeldClass)
admin.site.register(models.Schedule)
