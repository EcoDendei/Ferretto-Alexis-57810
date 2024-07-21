# importing datetime module 
import datetime 

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from .models import *


class AsientoForm(forms.Form):
    '''
    usuario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        to_field_name='username',
        required=True,  
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Usuario"
    )
    '''
    fecha = forms.DateField(initial=datetime.date.today,required=True)
    desc = forms.CharField(required=True)
    cuenta_origen = forms.ModelChoiceField(
        queryset=Subcuenta.objects.all(),
        to_field_name='nombre',
        required=True,  
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Cuenta Origen"
    )
    monto_origen = forms.FloatField(label="Monto Origen")
    cuenta_destino = forms.ModelChoiceField(
        queryset=Subcuenta.objects.all(),
        to_field_name='nombre',
        required=True,  
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Cuenta Destino"
    )
    monto_destino = forms.FloatField(label="Monto Destino")
    activo = forms.BooleanField(required=True, initial=True)


class LoginForm(AuthenticationForm):
    
    """ Form personalizado para el login de usuarios, esto para poder setear la clase que necesito para que tome bien el estilo. 
    Ademas al cargar la página se pone_el foco ya en el campo usuario.
    """
    
    username = UsernameField(label="Usuario", widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control', 'id': 'inputUsername'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ["username", "password"]
    
    
class RegistroForm(UserCreationForm):
    
    """ Form personalizado para el registro de usuarios, esto para poder setear la clase que necesito para que tome bien el estilo. 
    Ademas al cargar la página se pone_el foco ya en el campo usuario.
    """
    username = UsernameField(label="Usuario", widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control', 'id': 'inputUsername'}))
    first_name = forms.CharField(label="Nombre", required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputFirstName'}))
    last_name = forms.CharField(label="Apellido", required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputLastName'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'inputEmail'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputPassword'}))
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputPasswordConfirm'}))
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        
        
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)