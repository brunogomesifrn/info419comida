from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import receita

@login_required
def perfil(request):
	return render(request, 'perfil.html')

def registro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
		'form': form
	}
	return render(request, 'registro.html', contexto)

@login_required
def dados(request, id):
	user = User.objects.get(pk=id)
	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	contexto = {
		'form': form
	}
	return render(request, 'registro.html', contexto)

def receita(request):
	receita = recita.objects.all()
	contexto = {
		'lista_receitas': receita
	}
	return render(request, 'registro.html', contexto)

def tipo(request):
	return render(request, 'tipo.html')

def index(request):
	return render(request, 'index.html')


def login(request):
	return render(request, 'index.html')
