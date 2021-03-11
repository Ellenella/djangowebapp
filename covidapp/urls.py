from django.contrib import admin
from django.urls import path
from .views import helloview
urlpatterns = [
    path('',helloview),
]
