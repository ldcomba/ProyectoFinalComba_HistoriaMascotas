from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from .models import Mascota

class MascotaForm(forms.ModelForm):
 
 
    historia = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}), required=True )

    class Meta:
        model = Mascota
        fields = ['mascota', 'nombreMascota', 'titulo', 'historia'] #, 'imagenMascota'
        labels = {
            'nombreMascota': 'Nombre de la Mascota',
            'imagenMascota': 'Imagen de la Mascota',
        }




