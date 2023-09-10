from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        help_texts={k:"" for k in fields}




class UserEditForm(UserChangeForm,forms.Form):
    email= forms.EmailField(label="Email Usuario")
    password= forms.CharField(label="Contraseña Actual", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre',required=False)
    last_name=forms.CharField(label='Modificar Apellido',required=False)
    imagen = forms.ImageField(label="imagen", required=False)  # Campo de imagen no obligatorio
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción sobre usted',required=False)
    linkPaginaWeb=forms.URLField(label='Su red social',required=False,widget=forms.TextInput(attrs={'style': 'width: 500px;'}))
      
    class Meta:
        model=User
        fields = ["email", "password","first_name", "last_name"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor
    


class CambiarContrasegnaForm(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña Actual", widget=forms.PasswordInput(attrs={'style': 'height: 50px;'}))
    new_password1 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput(attrs={'style': 'height: 50px;'}))
    new_password2 = forms.CharField(label="Repetir nueva contraseña", widget=forms.PasswordInput(attrs={'style': 'height: 50px;'}))

class ChatForm (forms.Form):

    #mensaje= forms.CharField(label='Escriba su mensaje',required=False,widget=forms.Textarea)
    mensaje = forms.CharField(label='Escriba su mensaje', required=False, widget=forms.Textarea(attrs={'rows': 3}))

    # first_name=forms.CharField(label='Modificar Nombre',required=False)
    # last_name=forms.CharField(label='Modificar Apellido',required=False)
    # imagen = forms.ImageField(label="imagen", required=False)  # Campo de imagen no obligatorio
    # descripcion = forms.CharField(widget=forms.Textarea, label='Descripción sobre usted',required=False)
    # #linkPaginaWeb=forms.URLField(label='Su red social',required=False,widget=forms.TextInput(attrs={'style': 'width: 500px;'}))  