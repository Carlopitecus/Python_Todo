from django.urls import path
from .views import *

app_name = 'app'


urlpatterns = [

    path ('', home, name = 'home'),
    path('tareas/', tareas, name = 'tareas'),
    path('tareasProgreso/', tareasProgreso, name = 'tareasProgreso'),
    path('tareasCompleta/', tareasCompleta, name = 'tareasCompleta'),
    path('register/', register, name = 'register'),
    path('exit/', exit, name = 'exit'),
    path('tareas/ingresarTarea/', ingresarTarea, name = 'ingresarTarea'),
    path('tareas/editar/<int:id>/', editar, name = 'editar'),
    path('eliminar/<int:id>',eliminar, name= 'eliminar'),
    
    
]

