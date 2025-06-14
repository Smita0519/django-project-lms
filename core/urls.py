from django.urls import path
from core import views

urlpatterns =  [
    path('', views.home, name = 'home')     # '' no name means takes base url
]