from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, TareaForm
from .models import *
from datetime import date


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
    estado = 'Pendientes'
    usuario = request.user    
    tareas = Tarea.objects.filter(usuario=usuario).filter(estado='Pendiente').order_by('fechaTermino')
    count_pendientes = tareas.count()

    fecha_actual = date.today()
    tareasPendientes_vencidas = Tarea.objects.filter(fechaTermino__lt=fecha_actual)
    count_pendientesVencidas = tareasPendientes_vencidas.count()

    

    tareas_en_progreso = Tarea.objects.filter(usuario=usuario).filter(estado='En Progreso').order_by('fechaTermino')
    count_penprogreso = tareas_en_progreso.count()

    tareas_completadas = Tareacompletada.objects.filter(usuario=usuario).order_by('fechaCompletada')
    count_completadas = tareas_completadas.count()

    
   
    return render(request, 'tareas.html', {'tareas':tareas, 'count_pendientes':count_pendientes, 'count_penprogreso':count_penprogreso, 'count_completadas':count_completadas, 'count_pendientesVencidas':count_pendientesVencidas, 'estado':estado  })

@login_required
def tareasProgreso(request):
    estado = 'En progreso'
    usuario = request.user
    tareas_en_progreso = Tarea.objects.filter(usuario=usuario).filter(estado='En Progreso').order_by('fechaTermino')
    count_penprogreso = tareas_en_progreso.count()

    fecha_actual = date.today()
    tareasPendientes_vencidas = Tarea.objects.filter(fechaTermino__lt=fecha_actual)
    count_pendientesVencidas = tareasPendientes_vencidas.count()

    tareas = Tarea.objects.filter(usuario=usuario).filter(estado='Pendiente')
    count_pendientes = tareas.count()    

    tareas_completadas = Tareacompletada.objects.filter(usuario=usuario)
    count_completadas = tareas_completadas.count()
    return render(request, 'tareas.html', {'tareas' : tareas_en_progreso, 'count_pendientes':count_pendientes, 'count_penprogreso':count_penprogreso, 'count_completadas':count_completadas, 'count_pendientesVencidas':count_pendientesVencidas, 'estado':estado   })

@login_required
def tareasCompleta(request):
    estado = 'Completadas'
    usuario = request.user
    tareas_completadas = Tareacompletada.objects.filter(usuario=usuario).order_by('fechaCompletada')
    count_completadas = tareas_completadas.count()

    fecha_actual = date.today()
    tareasPendientes_vencidas = Tarea.objects.filter(fechaTermino__lt=fecha_actual)
    count_pendientesVencidas = tareasPendientes_vencidas.count()
    
    tareas_en_progreso = Tarea.objects.filter(usuario=usuario).filter(estado='En Progreso')
    count_penprogreso = tareas_en_progreso.count()

    tareas = Tarea.objects.filter(usuario=usuario).filter(estado='Pendiente')
    count_pendientes = tareas.count()     
    return render(request, 'tareas.html', {'tareas' : tareas_completadas, 'count_pendientes':count_pendientes, 'count_penprogreso':count_penprogreso, 'count_completadas':count_completadas, 'count_pendientesVencidas':count_pendientesVencidas, 'estado':estado  })

@login_required
def tareasVencidas(request):
    estado = 'Vencidas'
    usuario = request.user
    fecha_actual = date.today()
    tareasPendientes_vencidas = Tarea.objects.filter(fechaTermino__lt=fecha_actual).order_by('fechaTermino')
    count_pendientesVencidas = tareasPendientes_vencidas.count()

    tareas_completadas = Tareacompletada.objects.filter(usuario=usuario).order_by('fechaCompletada')
    count_completadas = tareas_completadas.count()    
    
    tareas_en_progreso = Tarea.objects.filter(usuario=usuario).filter(estado='En Progreso')
    count_penprogreso = tareas_en_progreso.count()

    tareas = Tarea.objects.filter(usuario=usuario).filter(estado='Pendiente')
    count_pendientes = tareas.count()     
    return render(request, 'tareas.html', {'tareas' : tareasPendientes_vencidas, 'count_pendientes':count_pendientes, 'count_penprogreso':count_penprogreso, 'count_completadas':count_completadas, 'count_pendientesVencidas':count_pendientesVencidas, 'estado':estado  })

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
    formulario = TareaForm(instance=tarea)
    

    if request.method == 'POST':   
        estado = request.POST.get('estado') 
        tarea.estado=estado             
        if tarea.estado == 'Completada':            
        # Crea una nueva instancia de TareaCompletada con los mismos datos
            tarea_completada = Tareacompletada(
            titulo=tarea.titulo,
            descripcion=tarea.descripcion,
            fechaCompletada=tarea.fechaTermino,
            categoria=tarea.categoria,
            usuario=tarea.usuario
            )
            tarea_completada.save() 
            tarea.delete()  # Elimina la tarea de Tarea
            
            return redirect('app:tareas')
                
        form = TareaForm(request.POST, instance=tarea)
        form.save()
        return redirect('app:tareas')
    return render(request, 'editar.html', {'formulario' : formulario})    
   
def eliminar(request, id):
    tarea = Tarea.objects.get(id = id)
    tarea.delete()
    return redirect('app:tareas')

def exit(request):
    logout(request)
    return redirect('app:home')
