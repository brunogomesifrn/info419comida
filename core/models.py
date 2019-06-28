from django.db import models

class Tipo(models.Model):
	tipox = models.CharField('Tipo da receita', primary_key=True, max_length=30)

class receita(models.Model):
	titulo = models.CharField('Nome da receita', primary_key=True, max_length=30)
	ingrediente = models.TextField('Ingredientes')
	preparo = models.TextField('Modo de preparo')
	imagem = models.ImageField('Imagem', upload_to='imagem', null=True)
	tipox = models.ForeignKey('tipo', on_delete=models.PROTECT)

	
# Create your models here.
