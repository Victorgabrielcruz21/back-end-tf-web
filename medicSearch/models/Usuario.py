# usuario.py
from django.db import models

class Usuario(models.Model):
    Vinculo_Escolar = models.CharField(max_length=200)
    Tipo_Usuario = models.CharField(max_length=200)
    ID = models.AutoField(primary_key=True)
    Email = models.EmailField(max_length=200, unique=True)
    Senha = models.CharField(max_length=200)
    Nome = models.CharField(max_length=200)
