from django.shortcuts import render
from django.http import HttpResponse

def tabela(request):
    return render(request, 'tabela.html')

# Create your views here.

