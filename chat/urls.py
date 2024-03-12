from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('checkview', views.checkview, name='checkview'),
    path('<str:room>/', views.room, name='room'),
    path('getMessages/<str:room>/',views.getMessages, name='getMessages'),
    path('send',views.sendMessages, name='send'),
]