from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .models import PerfilUsuario #Curso, Profesor, Estudiante, Avatar
from .forms import RegistroUsuarioForm,UserEditForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


# Create your views here.
def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "01_home.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "01_login.html", {"form":form, "mensaje":"Datos Invalidos"})
        else:
            return render(request, "01_login.html", {"form":form, "mensaje":"Datos Invalidos"})
    else:
        form=AuthenticationForm()
        return render(request, "01_login.html", {"form":form})
    

def register(request):
        if request.method == 'POST':
            form = RegistroUsuarioForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                form.save()
                return render(request, "01_home.html", {"mensaje":"Usuario Creado :)"})
            
            else:
                form=RegistroUsuarioForm()
                return render(request,"02_register.html", {"form":form,"mensaje":"Datos invalidos"})
        else:
            form=RegistroUsuarioForm()
        return render(request,"02_register.html", {"form":form})   


def editarPerfil(request):
    usuario=request.user
    perfilUsuario=PerfilUsuario.objects.filter(user=request.user.id)
    #perfilUsuario=PerfilUsuario.objects.get(user=request.user.id)
    #perfilUsuario, created = PerfilUsuario.objects.get_or_create(user=request.user.id)
    #perfilUsuario, created = PerfilUsuario.objects.get_or_create(user=request.user)
    if len(perfilUsuario)!=0:
        perfilUsuario = perfilUsuario[0]
    else:
        perfilUsuario = PerfilUsuario.objects.create(user=request.user)

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            #usuario.password1=info["password1"]
            #usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()

            if "imagen" in request.FILES:
                # avatarViejo=perfilUsuario.objects.filter(user=request.user)
                # if len(avatarViejo)>0:
                #     avatarViejo[0].delete()
                if perfilUsuario.imagen:
                    default_storage.delete(perfilUsuario.imagen.name)
                perfilUsuario.imagen = request.FILES["imagen"]
            
            perfilUsuario.linkPaginaWeb=info["linkPaginaWeb"]
            perfilUsuario.descripcion=info["descripcion"]
            perfilUsuario.save()

            return render(request,"01_home.html",{"mensaje": f"usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "03_editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "mensaje":"Datos invalidos"})
    else:
        mensaje=""
        form=UserEditForm(instance=usuario,initial={"descripcion":perfilUsuario.descripcion,"linkPaginaWeb":perfilUsuario.linkPaginaWeb,"imagen":perfilUsuario.imagen})
    
        return render(request, "03_editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "mensaje":mensaje})        