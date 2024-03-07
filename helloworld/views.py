from django.shortcuts import render

# Create your views here.
# helloworld/views.py

from django.http import HttpResponse


def hello_world_api(request):
    return HttpResponse("Hello World", content_type="text/plain")


def hello_world_api_v2(request):
    return HttpResponse("Hello World V2", content_type="text/plain")
