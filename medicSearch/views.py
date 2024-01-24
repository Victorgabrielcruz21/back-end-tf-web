import json
from .models import Usuario
from .models import Admin
from .models.Fila import Fila
from .models import Cardapio
from .models.Fila import Position

from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Usuario, Admin
from .serializers import UsuarioSerializer, AdminSerializer, FilaSerializer, CardapioSerializer
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

@api_view(['POST'])
@permission_classes([AllowAny])
def create_queue(request):
    if request.method == 'POST':
        serializer = FilaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_queues(request):
    if request.method == 'GET':
      queues = Fila.objects.all()
      serializer = FilaSerializer(queues, many=True)
      return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_queue(request, queue_id):
    if request.method == 'GET':
      try:
        queue = Fila.objects.get(id=queue_id)
        serializer = FilaSerializer(queue, many=False)
        return Response(serializer.data)
      except Fila.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['PUT'])
@permission_classes([AllowAny])
def update_queue(request, queue_id):
    if request.method == 'PUT':
      try: 
        queue = get_object_or_404(Fila, id=queue_id)
        data = json.loads(request.body)
        queue.nome = data.get('nome', queue.nome)
        queue.tamanho = data.get('tamanho', queue.tamanho)
        queue.save()
        serializer = FilaSerializer(queue, many=False)
        return Response(serializer.data)
      except Exception as ex:
        print(f"Erro inesperado: {ex}")
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_queue(request, queue_id):
    if request.method == 'DELETE':
        queue = get_object_or_404(Fila, id=queue_id)
        queue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

@api_view(['POST'])
@permission_classes([AllowAny])
def create_menu_item(request):
    if request.method == 'POST':
      serializer = CardapioSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_menu_items(request):
    if request.method == 'GET':
        cardapio = Cardapio.objects.all()
        serializer = CardapioSerializer(cardapio, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_menu_item(request, cardapio_id):
    if request.method == 'GET':
        try:
           
          cardapio = Cardapio.objects.get(id=cardapio_id)
          serializer = CardapioSerializer(cardapio, many=False)
          return Response(serializer.data)
        except Fila.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)
  
@api_view(['PUT'])
@permission_classes([AllowAny])
def update_menu_item(request, menu_item_id):
    if request.method == 'PUT':
        try:           
          menu_item = get_object_or_404(Cardapio, id=menu_item_id)
          data = json.loads(request.body)
          menu_item.link = data.get('link', menu_item.link)
          menu_item.save()
          serializer = CardapioSerializer(menu_item, many=False)
          return Response(serializer.data)
        except Exception as ex:
          print(f"Erro inesperado: {ex}")
          return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_cardapio(request, menu_item_id):
    if request.method == 'DELETE':
        menu_item = get_object_or_404(Cardapio, id=menu_item_id)
        menu_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([AllowAny])
def join_queue(request):
    if request.method == 'POST':
        student_id = request.data['student_id']
        student = get_object_or_404(Usuario, ID=student_id)
        queue = Fila.objects.first() # Supondo que exista apenas uma fila
        Position.objects.create(aluno=student, fila=queue, posicao=queue.posicao_set.count())
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def check_position(request):
    if request.method == 'GET':
        student_id = request.query_params['student_id']
        student = get_object_or_404(Usuario, ID=student_id)
        position = Position.objects.get(aluno=student).posicao
        return Response({'position': position}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def leave_queue(request):
    if request.method == 'DELETE':
        student_id = request.data['student_id']
        student = get_object_or_404(Usuario, ID=student_id)
        Position.objects.get(aluno=student).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


