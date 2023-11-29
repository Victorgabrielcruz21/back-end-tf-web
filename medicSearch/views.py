import json
from .models import Usuario
from .models import Admin

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Usuario, Admin
from .serializers import UsuarioSerializer, AdminSerializer
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializers import UsuarioSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404 , redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



@api_view(['GET'])
@permission_classes([AllowAny])
def usuario_list(request):
  if request.method == 'GET':
      usuarios = Usuario.objects.all()
      serializer = UsuarioSerializer(usuarios, many=True)
      return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def usuario_add(request):
   if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def usuario(request, user_id):
  if request.method == 'GET':
    try:
      usuario = Usuario.objects.get(ID=user_id)
      serializer = UsuarioSerializer(usuario, many=False)
      return Response(serializer.data)
    except Usuario.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
  elif request.method == 'PUT':
    try:
      usuario = get_object_or_404(Usuario, ID=user_id)
      data = json.loads(request.body)
      usuario.Vinculo_Escolar = data.get('Vinculo_Escolar', usuario.Vinculo_Escolar)
      usuario.Tipo_Usuario = data.get('Tipo_Usuario', usuario.Tipo_Usuario)
      usuario.Email = data.get('Email', usuario.Email)
      usuario.Senha = data.get('Senha', usuario.Senha)
      usuario.Nome = data.get('Nome', usuario.Nome)
      usuario.save()
      serializer = UsuarioSerializer(usuario, many=False)
      return Response(serializer.data)
    except Exception as ex:
      print(f"Erro inesperado: {ex}")
      return Response(status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    try:
      usuario = get_object_or_404(Usuario, ID=user_id)
      usuario.delete()
    except Exception as ex:
      print(f"Erro inesperado: {ex}")


@api_view(['GET'])
@permission_classes([AllowAny])
def admin_list(request):
  if request.method == 'GET':
    admins = Admin.objects.all()
    serializer = AdminSerializer(admins, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def admin_add(request):
   if request.method == 'POST':
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def admin(request, admin_id):
  if request.method == 'GET':
    try:
      admin = Admin.objects.get(ID=admin_id)
      serializer = AdminSerializer(admin, many=False)
      return Response(serializer.data)
    except Admin.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
  elif request.method == 'PUT':
    try:
      admin = get_object_or_404(Admin, ID=admin_id)
      data = json.loads(request.body)
      admin.Vinculo_Escolar = data.get('Vinculo_Escolar', admin.Vinculo_Escolar)
      admin.Email = data.get('Email', admin.Email)
      admin.Senha = data.get('Senha', admin.Senha)
      admin.Nome = data.get('Nome', admin.Nome)
      admin.save()
      serializer = AdminSerializer(admin, many=False)
      return Response(serializer.data)
    except Exception as ex:
      print(f"Erro inesperado: {ex}")
      return Response(status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    try:
      admin = get_object_or_404(Admin, ID=admin_id)
      admin.delete()
      return Response({'something': 'Foi'})

    except Exception as ex:
      print(f"Erro inesperado: {ex}")
