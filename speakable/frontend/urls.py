from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
  path('', views.index, name='index'),
  path('room/<str:room_name>/', views.room, name='room'),
  path('about/', views.about, name='about'),
]
