"""
URL configuration for medicSearchAdmin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from medicSearch.views import usuario_add,  usuario_list, usuario, admin_list, admin_add, admin
from django.urls import path



urlpatterns = [
    path('usuario/', usuario_add),
    path('usuario/<int:user_id>/', usuario, name='usuario'),
    path('usuarios/', usuario_list, name='usuarios'),
    path('admin/', admin_add),
    path('admin/<int:admin_id>/', admin, name='admin'),
    path('admins/', admin_list, name='admins')

]