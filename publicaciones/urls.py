from django.urls import path
from .views import listar_publicaciones, crear_publicacion, editar_publicacion, eliminar_publicacion

urlpatterns = [
    path('', listar_publicaciones, name='listar_publicaciones'),
    path('nueva/', crear_publicacion, name='crear_publicacion'),
    path('editar/<int:id>/', editar_publicacion, name='editar_publicacion'),
    path('eliminar/<int:id>/', eliminar_publicacion, name='eliminar_publicacion'),
]
