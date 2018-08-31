from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return HttpResponse ("Something was done")

# Create your views here.

