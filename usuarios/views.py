from django.shortcuts import render, redirect
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        Usuario.objects.create(nombre=nombre, correo=correo)
        return redirect('listar_usuarios')
    return render(request, 'usuarios/crear_usuario.html')
