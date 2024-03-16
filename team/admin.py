from django.contrib import admin
from . import models

admin.site.register(models.JobPosition)
admin.site.register(models.Trainer)
admin.site.register(models.SportActivity)
admin.site.register(models.TrainerComment)