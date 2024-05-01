from django.shortcuts import render
from django.http import HttpResponse

def quiz_qu_view(request):
    return HttpResponse('<h1>from quiz_qu_view</h1>')
