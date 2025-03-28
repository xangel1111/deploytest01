from django.urls import path
from .views import listar_usuarios, crear_usuario

urlpatterns = [
    path('', listar_usuarios, name='listar_usuarios'),
    path('nuevo/', crear_usuario, name='crear_usuario'),
]
