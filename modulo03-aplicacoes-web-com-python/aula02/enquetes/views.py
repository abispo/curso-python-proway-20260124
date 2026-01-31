from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Você está na página principal das enquetes.")