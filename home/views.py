from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

from datetime import date
from django.shortcuts import render

def home(request):
    data_atual = date.today()
    jogos = [
        {'time': 'Barcelona x Real Madrid', 'dia': 'sexta-feira |','horario': 'às 12h00'},
        {'time': 'Arsenal x Liverpool', 'dia': 'sexta-feira |','horario': 'às 15h00'},
        {'time': 'Flamengo x Palmeiras', 'dia': 'sábado |','horario': 'às 8h00'},
        {'time': 'PSG x Bayern', 'dia': 'sábado |','horario': 'às 20h00'}
    ] # lista de jogos previstos para o dia
    return render(request, 'home.html', {'data_atual': data_atual, 'jogos': jogos})


# Create your views here.
