from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
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

def receitax(request):
	receitas = receita.objects.all()
	contexto = {
		'lista_receitas': receitas
	}
	return render(request, 'receita.html', contexto)

def tipo(request):
	return render(request, 'tipo.html')

def index(request):
	return render(request, 'index.html')



