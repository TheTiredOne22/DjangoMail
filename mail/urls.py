from django.urls import path
from . import views

app_name = 'mail'

urlpatterns = [
    path('', views.index, name='index'),
    path('compose/', views.compose, name='compose'),
    path('read/', views.read, name='read'),
    path('reply/', views.reply, name='reply')
]
