from rest_framework import serializers
from .models import Usuario, Admin

class UsuarioSerializer(serializers.ModelSerializer):
   class Meta:
       model = Usuario
       fields = ['Vinculo_Escolar', 'Tipo_Usuario', 'ID', 'Email', 'Senha', 'Nome']

class AdminSerializer(serializers.ModelSerializer):
   class Meta:
       model = Admin
       fields = ['Vinculo_Escolar', 'ID', 'Email', 'Senha', 'Nome']
