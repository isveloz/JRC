# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Producto, Tarea

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, help_text='Opcional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Opcional')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['direccion', 'telefono', 'fecha_nacimiento']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
#class BoletaForm(forms.ModelForm):
#    class Meta:
#        model = Boleta
#        fields = ['id_boleta', 'cliente', 'monto', 'fecha']