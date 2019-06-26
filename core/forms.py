from django.forms import ModelForm
from .models import receita

class receitaForm(ModelForm):
	class Meta():
		models = receita.objectos
		fields = ['']#parei aqui