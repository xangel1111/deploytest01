from django.shortcuts import render, redirect
from .models import Publicacion
from usuarios.models import Usuario

def listar_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'publicaciones/listar_publicaciones.html', {'publicaciones': publicaciones})

def crear_publicacion(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        usuario_id = request.POST.get('usuario')
        usuario = Usuario.objects.get(id=usuario_id)
        Publicacion.objects.create(titulo=titulo, contenido=contenido, usuario=usuario)
        return redirect('listar_publicaciones')
    usuarios = Usuario.objects.all()
    return render(request, 'publicaciones/crear_publicacion.html', {'usuarios': usuarios})

def editar_publicacion(request, id):
    publicacion = Publicacion.objects.get(id=id)
    if request.method == "POST":
        publicacion.titulo = request.POST.get('titulo')
        publicacion.contenido = request.POST.get('contenido')
        publicacion.usuario_id = request.POST.get('usuario')
        publicacion.save()
        return redirect('listar_publicaciones')
    
    usuarios = Usuario.objects.all()
    return render(request, 'publicaciones/editar_publicacion.html', {'publicacion': publicacion, 'usuarios': usuarios})

def eliminar_publicacion(request, id):
    publicacion = Publicacion.objects.get(id=id)
    if request.method == "POST":
        publicacion.delete()
        return redirect('listar_publicaciones')
    
    return render(request, 'publicaciones/eliminar_publicacion.html', {'publicacion': publicacion})