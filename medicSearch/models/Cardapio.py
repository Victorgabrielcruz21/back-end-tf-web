from django.db import models

class Cardapio(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.URLField(null=True, blank=True)

    