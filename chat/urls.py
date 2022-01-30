# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('chat/', views.IndexView.as_view(), name ='index'),
    path('room/', views.RoomView.as_view(), name='room'),
    
    path('get_token/', views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    
]