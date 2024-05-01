from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Home... theke bolchi</h1>")
