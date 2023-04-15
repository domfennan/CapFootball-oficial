from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.messages import constants
from django.contrib import messages

from register.models import Register

def load(request):
        return render(request, 'register.html')


def cadastro(request):
        vnome = request.POST.get('name')
        vemail = request.POST.get('email')
        vsenha = request.POST.get('senha')

        try:
                user = Register(nome=vnome,email=vemail,senha=vsenha,)
                user.save()
                return redirect('/home/login/')
        except:
                messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
                return redirect('/load/')
        return HttpResponse(f"{nome}, {email}, {senha}")



