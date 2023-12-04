from django.contrib import admin
from django.urls import path
from .views import test_list

urlpatterns = [
    path('tests/', test_list, name='test_list'),
]
