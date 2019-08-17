from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def hello_world(request):
    return HttpResponse("Hello, World!")


def index(request):
    return render(request, "app.html", {'BUNDLED': settings.BUNDLED})
    # return HttpResponse("Hello, World!")
