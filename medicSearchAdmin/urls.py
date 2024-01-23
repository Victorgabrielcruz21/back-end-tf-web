from . import views

from medicSearch.views import usuario_add,  usuario_list, usuario, admin_list, admin_add, admin
from django.urls import path



urlpatterns = [
    path('usuario/', usuario_add),
    path('usuario/<int:user_id>/', usuario, name='usuario'),
    path('usuarios/', usuario_list, name='usuarios'),
    path('admin/', admin_add),
    path('admin/<int:admin_id>/', admin, name='admin'),
    path('admins/', admin_list, name='admins'),
    path('fila/', views.create_queue, name='create_queue'),
    path('fila/', views.get_queues, name='get_queues'),
    path('fila/<int:queue_id>/', views.get_queue, name='get_queue'),
    path('fila/<int:queue_id>/', views.update_queue, name='update_queue'),
    path('fila/<int:queue_id>/', views.delete_queue, name='delete_queue'),
    path('fila/join', views.join_queue, name='join_queue'),
    path('fila/position', views.check_position, name='check_position'),
    path('fila/leave', views.leave_queue, name='leave_queue'),
    path('cardapio/', views.create_menu_item, name='create_menu_item'),
    path('cardapio/', views.get_menu_items, name='get_menu_items'),
    path('cardapio/<int:menu_item_id>/', views.get_menu_item, name='get_menu_item'),
    path('cardapio/<int:menu_item_id>/', views.update_menu_item, name='update_menu_item'),
    path('cardapio/<int:menu_item_id>/', views.delete_menu_item, name='delete_menu_item'),

]