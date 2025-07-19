from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    pontos = models.IntegerField()

    def __str__(self):
        return self.nome
from django.db import models

# Create your models here.
