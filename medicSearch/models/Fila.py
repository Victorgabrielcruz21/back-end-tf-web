from django.db import models
from medicSearch.models import Usuario

class Fila(models.Model):
    alunos = models.ManyToManyField(Usuario, through='Posicao')
    nome = models.CharField(max_length=200)
    data_hora = models.DateTimeField()
    tamanho = models
    id = models.AutoField(primary_key=True)
    

class Posicao(models.Model):
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fila = models.ForeignKey(Fila, on_delete=models.CASCADE)
    posicao = models.IntegerField()