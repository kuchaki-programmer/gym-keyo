from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('list/', views.BlogListView.as_view(), name='blog_list_view'),
    path('detail/<int:pk>/',views.BlogDetailView.as_view(), name='blog_detail'),
    path('create_comment/<int:pk>', views.CreateCommentView.as_view(), name='create_blogcomment'),

]