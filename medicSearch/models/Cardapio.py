from django.db import models

class Cardapio(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.URLField()

    def __str__(self):
        return f'Cardapio {self.id}'