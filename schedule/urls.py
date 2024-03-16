from django.urls import path
from . import views

app_name = 'schedule'
urlpatterns = [
    path('', views.ScheduleView.as_view(), name='schedule_view'),
]