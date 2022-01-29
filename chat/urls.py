# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(), name ='index'),
    path('<str:room_name>/', views.RoomView.as_view(), name='room'),
]