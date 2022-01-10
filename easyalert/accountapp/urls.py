from django.contrib import admin
from django.urls import path, include
from accountapp.views import hello_world

# appName = 'accountapp'


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]
