from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator

# Create your models here.
class Mascota(models.Model):
    mascotaSeleccion= (
        ('gato','Gato'),
        ('perro','Perro'),
        ('pajaro','Pajaro'),
        ('pez','Pez'),
        ('otro','Otro')
    )
    autor=models.ForeignKey(User, on_delete=models.CASCADE,blank=False)
    mascota= models.CharField(max_length=50, choices=mascotaSeleccion, default='')
    nombreMascota=models.CharField(max_length=50, blank=False)
    titulo=models.CharField(max_length=50,blank=False)
    historia = models.TextField(
        validators=[MaxLengthValidator(limit_value=3200, message='La historia no puede superar 40 líneas.')],
        help_text="Ingresa la historia de la mascota (máximo 40 líneas)."
    )
    fechaPublicacion=models.DateTimeField(auto_now_add=True)
    imagenMascota = models.ImageField(null=True, blank=True, upload_to="imagenes/")
    
    class Meta:
        ordering = ['autor', '-fechaPublicacion']
   
    
    def __str__(self):
        return f'{self.autor} - {self.mascota} - {self.nombreMascota} - {self.titulo} '