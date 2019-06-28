from django.forms import ModelForm
from .models import receita

class receitaForm(ModelForm):
	class Meta:
		model = receita
		fields = ['titulo', 'ingrediente', 'preparo', 'imagem' ]#parei aqui