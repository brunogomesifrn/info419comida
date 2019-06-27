from django.db import models

class receita(models.Model):
	titulo = models.CharField('Nome da receita:', max_length=100)
	ingrediente = models.TextField('Ingredientes:')
	preparo = models.TextField('Modo de preparo:')
	imagem = models.ImageField('Imagem', upload_to='imagem', null=True)

	
# Create your models here.
