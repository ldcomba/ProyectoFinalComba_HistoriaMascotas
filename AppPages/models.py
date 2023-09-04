from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mascota(models.Model):
    mascotaSeleccion= (
        ('gato','Gato'),
        ('perro','Perro'),
        ('pajaro','Pajaro'),
        ('pez','Pez'),
        ('otro','Otro')
    )
    autor=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mascota= models.CharField(max_length=50, choices=mascotaSeleccion, default='gato')
    nombreMascota=models.CharField(max_length=50)
    titulo=models.CharField(max_length=50)
    historia=models.CharField(max_length=40*80)
    fechaPublicacion=models.DateTimeField(auto_now_add=True)
    imagenMascota = models.ImageField(null=True, blank=True, upload_to="imagenes/")
    
    class Meta:
        ordering = ['autor', '-fechaPublicacion']
   
    
    def __str__(self):
        return self.titulo