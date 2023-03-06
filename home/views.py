from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

from datetime import date
from django.shortcuts import render

def home(request):
    data_atual = date.today()
    jogos = [
        {'time': 'Barcelona x Real Madrid', 'horario': '12h00'},
        {'time': 'Arsenal x Liverpool', 'horario': '15h00'},
        {'time': 'Flamengo x Palmeiras', 'horario': '18h00'},
        {'time': 'garra x cap', 'horario': '20h00'}
    ] # lista de jogos previstos para o dia
    return render(request, 'home.html', {'data_atual': data_atual, 'jogos': jogos})


# Create your views here.
