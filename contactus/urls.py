from django.urls import path
from . import views

app_name = 'contact_us'
urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contactus_view'),
    path('done/', views.DoneView.as_view(), name="done"),
]