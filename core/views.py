from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import receita, Tipo
from .forms import receitaForm, TipoForm

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

def tipox(request):
	tipu = Tipo.objects.all()
	contexto = {
		'lista_tipu': tipu
	}
	return render(request, 'tipo.html', contexto)

def cadastrar_tipo(request):
	form = TipoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('tipo')
	contexto = {
		'form': form
	}
	return render(request, 'cadastrar_tipo.html', contexto)

def index(request):
	return render(request, 'index.html')

def cadastrar_receita(request):
	form = receitaForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('receita')

	contexto = {
		'form' : form
	}
	return render(request, 'cadastrar_receita.html', contexto)




