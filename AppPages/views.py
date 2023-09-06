from django.shortcuts import render
from .models import Mascota

#from .models import Impresora, RolloFilamento, Archivo3mf   
from django.http import HttpResponse
#from .forms import ImpresoraForm, RolloFilamentoForm, Archivo3mfForm

# Create your views here.
def home (request):
    return render(request,"01_home.html")

def aboutMe (request):
    return render(request,"02_aboutMe.html")


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

    return render(request, "03_routePages.html",{"mascotasHistorias":mascotasHistorias,"mensaje":mensaje})


def routePagesId (request,id):
    mascotasHistorias=Mascota.objects.get(id=id)
    if len(mascotasHistorias.imagenMascota)==0:
        mensaje= "Esta publicación no tiene imagen comunicarse con el admin"
    else:
        mensaje=""
    
    return render(request, "04_routePagesId.html",{"mascotasHistorias":mascotasHistorias,"mensaje":mensaje})


