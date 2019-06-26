from django.db import models

class receita(models.Model):
	receita = models.CharField('Nome da receita:', max_length=100)

# Create your models here.
