# helloworld/urls.py

from django.urls import path
from .views import hello_world_api, hello_world_api_v2

urlpatterns = [
    path('hello/', hello_world_api),
    path('hello/v2', hello_world_api_v2),
]
