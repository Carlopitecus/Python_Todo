from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, TareaForm
from .models import *


# Create your views here.
def home (request):
    return render(request, 'home.html')

def register(request):
    data = {
        'form': UsuarioForm()
    }

    if request.method == 'POST':
        user_creation_form = UsuarioForm(data = request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username = user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('app:home')

    return render(request, 'registration/register.html', data)

@login_required
def tareas(request):
    usuario = request.user
    
    tareas = Tarea.objects.filter(usuario=usuario).filter(estado='Pendiente').order_by('fechaTermino')
   
    return render(request, 'tareas.html', {'tareas' : tareas})

@login_required
def tareasProgreso(request):
    usuario = request.user
    tareas_en_progreso = Tarea.objects.filter(usuario=usuario).filter(estado='En Progreso').order_by('fechaTermino')
    return render(request, 'tareas.html', {'tareas' : tareas_en_progreso})

@login_required
def tareasCompleta(request):
    usuario = request.user
    tareas_completadas = Tarea.objects.filter(usuario=usuario).filter(estado='Completada').order_by('fechaTermino')
    return render(request, 'tareas.html', {'tareas' : tareas_completadas})

@login_required
def ingresarTarea(request):
    if request.method == 'POST':

        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fechaTermino = request.POST.get('fechaTermino')
        categoria = request.POST.get('categoria')
        usuario = request.user

        tarea = Tarea.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            fechaTermino=fechaTermino,
            categoria=categoria,
            usuario=usuario        )

        tarea.save()
        return redirect('app:tareas')
    return render(request, 'ingresarTarea.html')


def editar(request, id):
    tarea = Tarea.objects.get(id = id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fechaTermino = request.POST.get('fechaTermino')
        categoria = request.POST.get('categoria')
        usuario = request.user

        tarea = Tarea.objects.update(
            titulo=titulo,
            descripcion=descripcion,
            fechaTermino=fechaTermino,
            categoria=categoria,
            usuario=usuario        )

        #if tarea.is_valid():
        tarea.save()
            
        return redirect('app:tareas')
    return render(request, 'editar.html', {'tareas' : tarea} )    
   
def eliminar(request, id):
    tarea = Tarea.objects.get(id = id)
    tarea.delete()
    return redirect('app:tareas')

def exit(request):
    logout(request)
    return redirect('app:home')
