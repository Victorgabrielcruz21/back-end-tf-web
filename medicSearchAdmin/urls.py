from medicSearch.views import usuario_add,  usuario_list, usuario, admin_list, admin_add, admin, delete_cardapio, create_queue, get_queues, delete_queue, get_queue, update_queue, join_queue , check_position, leave_queue, create_menu_item, get_menu_items, get_menu_item, update_menu_item
from django.urls import path



urlpatterns = [
    path('usuario/', usuario_add),
    path('usuario/<int:user_id>/', usuario, name='usuario'),
    path('usuarios/', usuario_list, name='usuarios'),
    path('admin/', admin_add),
    path('admin/<int:admin_id>/', admin, name='admin'),
    path('admins/', admin_list, name='admins'),
    path('fila/', create_queue, name='create_queue'),
    path('filas/', get_queues, name='get_queues'),
    path('fila/<int:queue_id>/', get_queue, name='get_queue'),
    path('fila/<int:queue_id>/update', update_queue, name='update_queue'),
    path('fila/<int:queue_id>/delete', delete_queue, name='delete_queue'),
    path('fila/join', join_queue, name='join_queue'),
    path('fila/position', check_position, name='check_position'),
    path('fila/leave', leave_queue, name='leave_queue'),
    path('cardapio/', create_menu_item, name='create_menu_item'),
    path('cardapios/', get_menu_items, name='get_menu_items'),
    path('cardapio/<int:cardapio_id>/', get_menu_item, name='get_menu_item'),
    path('cardapio/<int:menu_item_id>/update', update_menu_item, name='update_menu_item'),
    path('cardapio/<int:menu_item_id>/delete', delete_cardapio, name='delete_cardapio'),

]
