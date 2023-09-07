from django.shortcuts import render
from .models import Mascota 
from AppAccounts.models import PerfilUsuario

#from .models import Impresora, RolloFilamento, Archivo3mf   
from django.http import HttpResponse
#from .forms import ImpresoraForm, RolloFilamentoForm, Archivo3mfForm
from django.db.models import Q
# Create your views here.


def obtenerAvatar(request):
    #avatares=PerfilUsuario.objects.filter(user=request.user.id)
    avatares = PerfilUsuario.objects.filter(Q(user=request.user.id) & Q(imagen__isnull=False) & ~Q(imagen=''))
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/media/avatars/avatarpordefecto.png"


def home (request):
    return render(request,"01_home.html",{"avatar":obtenerAvatar(request)})

def aboutMe (request):
    return render(request,"02_aboutMe.html",{"avatar":obtenerAvatar(request)})


def routePages(request):
    if request.method=="POST":
       pass
    else:
        mascotasHistorias=Mascota.objects.all()
        #mascotasHistorias=""
        if len(mascotasHistorias) == 0:
            mensaje= " Aún no hay historias"
        else:
            mensaje=""

    return render(request, "03_routePages.html",{"mascotasHistorias":mascotasHistorias,"mensaje":mensaje,"avatar":obtenerAvatar(request)})


def routePagesId (request,id):
    mascotasHistorias=Mascota.objects.get(id=id)
    if len(mascotasHistorias.imagenMascota)==0:
        mensaje= "Esta publicación no tiene imagen comunicarse con el admin"
    else:
        mensaje=""
    
    return render(request, "04_routePagesId.html",{"mascotasHistorias":mascotasHistorias,"mensaje":mensaje,"avatar":obtenerAvatar(request)})


