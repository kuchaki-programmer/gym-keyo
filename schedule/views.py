from django.shortcuts import render
from django.views.generic import View
from . import models


class ScheduleView(View):
    def get(self, request):
        week_days = models.WeekDay.objects.all()
        context = {
            'week_days': week_days
        }
        return render(request, 'schedule/schedule.html', context)