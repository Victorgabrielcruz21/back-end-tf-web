# Generated by Django 4.2.7 on 2024-01-24 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicSearch', '0003_fila_tamanho_alter_fila_data_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fila',
            name='alunos',
            field=models.ManyToManyField(blank=True, null=True, through='medicSearch.Position', to='medicSearch.usuario'),
        ),
    ]
