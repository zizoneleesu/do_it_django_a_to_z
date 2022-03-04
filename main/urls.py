from django.contrib import admin
from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path("main/", views.main, name="main"),
]