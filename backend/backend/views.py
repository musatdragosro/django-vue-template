from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse("Hello, World!")


def index(request):
    return render(request, "app.html")
    # return HttpResponse("Hello, World!")
