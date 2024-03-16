from django.db import models
from team.models import Trainer


class WeekDay(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class HeldClass(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.description[:15]}'


class Schedule(models.Model):
    held_class = models.ForeignKey(HeldClass, on_delete=models.CASCADE, related_name='schedules')
    week_day = models.ForeignKey(WeekDay, on_delete=models.CASCADE, related_name='schedules')
    trainer = models.ManyToManyField(Trainer, related_name='schedules')
    start_at = models.TimeField()
    end_at = models.TimeField()

    def __str__(self):
        return f'{self.held_class}-{self.week_day}'