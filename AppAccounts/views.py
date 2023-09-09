from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from .models import PerfilUsuario, Comentario #Curso, Profesor, Estudiante, Avatar
from .forms import RegistroUsuarioForm,UserEditForm,CambiarContrasegnaForm,ChatForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from AppPages.views import obtenerAvatar
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
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
                return render(request, "01_home.html", {"mensaje":f"Usuario {usu} logueado correctamente",  "avatar":obtenerAvatar(request)})
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
                return render(request, "01_home.html", {"mensaje":"Usuario Creado :)",  "avatar":obtenerAvatar(request)})
            
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
            password = info["password"]
            if not authenticate(username=usuario.username, password=password):
                return render(request,"03_editarPerfil.html",{"form": form,"nombreusuario": usuario.username,"mensaje": "Contraseña incorrecta" ,  "avatar":obtenerAvatar(request)})
            else:
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

                return render(request,"01_home.html",{"mensaje": f"usuario {usuario.username} editado correctamente",  "avatar":obtenerAvatar(request)})
        else:
            return render(request, "03_editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "mensaje":"Datos invalidos",  "avatar":obtenerAvatar(request)})
    else:
        mensaje=""
        form=UserEditForm(instance=usuario,initial={"descripcion":perfilUsuario.descripcion,"linkPaginaWeb":perfilUsuario.linkPaginaWeb,"imagen":perfilUsuario.imagen})
    
        return render(request, "03_editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "mensaje":mensaje,  "avatar":obtenerAvatar(request)})     

def chatRoom(request):
    usuarios = User.objects.exclude(username=request.user.username)
    #form=UserEditForm(request.POST)
    if request.method=="POST":
        posteo = request.POST.get('posteo')
        print(posteo)
        if posteo=="1" :
            usuario_seleccionado_id = request.POST.get('usuarios')
            receptorSeleccionado_id= usuario_seleccionado_id
            

        if posteo=="2":
            receptor = request.POST.get('receptor')
            receptorSeleccionado_id=receptor
            #print("Valor de receptor:", receptor)
            form=ChatForm(request.POST)
            if form.is_valid():
                info=form.cleaned_data
                emisor = request.user
                receptorSeleccionado = User.objects.get(id=receptorSeleccionado_id)
                receptor = receptorSeleccionado
                mensaje = info["mensaje"]
                leido= False
                fechaComentario = timezone.now().date()
                comentario=Comentario(emisor=emisor,receptor=receptor,mensaje=mensaje,leido=leido,fechaComentario=fechaComentario)
                comentario.save()

        

            #Comentario
            #mensasjesEntreEllos = Comentario.objects.filter(Q(emisor=request.user.id) & Q(receptor=usuario_seleccionado_id) )
        mensajesEntreEllos = Comentario.objects.filter(
    Q(emisor=request.user.id, receptor=receptorSeleccionado_id) | Q(emisor=receptorSeleccionado_id, receptor=request.user.id)
    ).order_by('fechaComentario')
        

        mensajesLeidos = Comentario.objects.filter(Q(emisor=receptorSeleccionado_id, receptor=request.user.id)).order_by('fechaComentario')
        for mensajeLeido in mensajesLeidos:
            mensajeLeido.leido=True
            mensajeLeido.save()

        
        chatFormulario= ChatForm()
        return render(request, "05_chatRoom.html", {'usuarios': usuarios, "receptorSeleccionado":receptorSeleccionado_id,"mensajesEntreEllos":mensajesEntreEllos,"chatFormulario":chatFormulario,"avatar":obtenerAvatar(request)})    
    else:
        return render(request, "05_chatRoom.html", {'usuarios': usuarios,"avatar":obtenerAvatar(request)})    
        









# def cambiarPass(request):
   
#     usuario = request.user
#     if request.method == "POST":
#         form = CambiarContrasegnaForm(request.POST)
#         if form.is_valid():
#             # Obtenemos la contraseña actual del formulario
#             old_password = form.cleaned_data['old_password']
#             # Verificamos que la contraseña actual sea correcta
#             if usuario.check_password(old_password):
#                 # Cambiamos la contraseña del usuario
#                 new_password = form.cleaned_data['new_password1']
#                 usuario.set_password(new_password)
#                 usuario.save()
#                 # Actualizamos la sesión de autenticación
#                 update_session_auth_hash(request, usuario)
#                 return render(request, "01_home.html", {"mensaje": f"Contraseña de {usuario.username} cambiada correctamente"})
#             else:
                
#                 return render(request, "04_cambiarPass.html", {"form": form, "nombreusuario": usuario.username, "mensaje": "Contraseña actual incorrecta"})
#         else:
#             mensaje=form.is_valid()
#             return render(request, "04_cambiarPass.html", {"form": form, "nombreusuario": usuario.username, "mensaje": mensaje})
#     else:
#         mensaje = ""
#         form = CambiarContrasegnaForm(usuario)
#         return render(request, "04_cambiarPass.html", {"form": form, "nombreusuario": usuario.username, "mensaje": mensaje})
    

class CambiarContrasenaView(SuccessMessageMixin,PasswordChangeView):
    template_name = '04_cambiarPass.html'  
    form_class = CambiarContrasegnaForm  # Utiliza tu formulario personalizado
    success_url =  reverse_lazy('home')  # Define la URL a la que redirigir después de cambiar la contraseña
    success_message = "Contraseña cambiada correctamente"  # Mensaje de éxito
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['avatar'] = obtenerAvatar(self.request) # Add the "avatar" variable to the context
            return context