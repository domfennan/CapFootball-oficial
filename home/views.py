from django.shortcuts import render, redirect

from register.models import Register


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

def login(request):
    return render(request, 'login.html')


def logado(request):
    vemail = request.POST.get('email')
    vsenha = request.POST.get('senha')

    usuario = Register.objects.get(email=vemail, senha=vsenha)

    if not usuario:
        return redirect('/login')
    else:
        return render(request,'home.html', {"usuario": usuario})

def dados(request, id):
    usuario = Register.objects.get(id=id)
    return render(request, 'dados.html', {"usuario":usuario})

def updados(request, id):

    vnome = request.POST.get("name")
    vemail = request.POST.get("email")
    vsenh = request.POST.get("senha")

    usuario = Register.objects.get(id=id)

    if vnome != "":
        usuario.nome=vnome
    if vemail != "":
        usuario.email=vemail
    if vsenh != "":
        usuario.senha=vsenh

    usuario.save()
    return render(request,'home.html', {"usuario": usuario})

def delete(request, id):
    usuario = Register.objects.get(id=id)
    usuario.delete()
    return redirect('/home/login/')