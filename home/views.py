from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('pagina home cumpade')
# Create your views here.
