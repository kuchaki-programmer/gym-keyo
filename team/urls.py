from django.urls import path
from . import views

app_name = 'team'
urlpatterns = [
    path('', views.TeamView.as_view(), name='team_view'),
    path('detail/<int:pk>/', views.TrainerDetail.as_view(), name='trainer_detail'),
    path('create_comment/<int:trainer_pk>/', views.CreateComment.as_view(), name='create_trainer_comment'),
]