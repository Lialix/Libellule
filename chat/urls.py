# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('chat/', views.IndexView.as_view(), name ='index'),
    path('chat/<str:room_name>/', views.RoomView.as_view(), name='room'),
    
    path('get_token/', views.getToken),
    
]