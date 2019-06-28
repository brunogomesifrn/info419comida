from django.forms import ModelForm
from .models import receita, Tipo


class receitaForm(ModelForm):
	class Meta:
		model = receita
		fields = ['titulo', 'ingrediente', 'preparo', 'imagem', 'tipox' ]#parei aqui