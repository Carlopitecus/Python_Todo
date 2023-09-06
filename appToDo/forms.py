from django import forms
from .models import Tarea, Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [ 'username', 'first_name', 'last_name','password1','password2' ]
        labels = {
            'username' : 'Nombre de usuario',
            'first_name' : 'Nombre',
            'last_name' : 'Apellido',
            'password1': 'Contraseña',
            'password2' : 'Repita la Contraseña'  
        }

class TareaForm(forms.ModelForm):
    
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fechaTermino','estado','categoria', ]
    
    def get_concrete_fields(self):
        return [field for field in self.get_fields() if field.concrete]