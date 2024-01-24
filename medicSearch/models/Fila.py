from django.db import models
from medicSearch.models import Usuario

class Fila(models.Model):
    alunos = models.ManyToManyField(Usuario, through='Position', null=True, blank=True)
    nome = models.CharField(max_length=200)
    data_hora = models.DateTimeField(auto_now_add=True)
    tamanho = models.IntegerField(default=100)
    id = models.AutoField(primary_key=True)

class Position(models.Model):
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fila = models.ForeignKey(Fila, on_delete=models.CASCADE)
    posicao = models.IntegerField()