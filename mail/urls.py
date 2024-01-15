from django.urls import path
from . import views

app_name = 'mail'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('sent/', views.sent, name='sent'),
    path('drafts/', views.draft, name='drafts'),
    path('archive/', views.archive, name='archive'),
    path('read/<slug:slug>/', views.read_email, name='read'),
    path('compose/', views.compose_email, name='compose'),
    # path('read/', views.read, name='read'),
    # path('reply/', views.reply, name='reply')

]
