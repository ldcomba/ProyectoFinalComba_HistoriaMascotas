from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.


class PerfilUsuario(models.Model):
    #vinculo con el usuario
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares de media
    imagen=models.ImageField(upload_to="avatars",null=True, blank=True)
    descripcion=models.CharField(max_length=500)
    linkPaginaWeb=models.URLField()
    
    def __str__(self):
         return f'Usuario: {self.user}  Página Web: {self.linkPaginaWeb}'





class Comentario(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE , related_name="usarioEmisor")
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usarioReceptor")
    mensaje = models.TextField(null=True, blank=True)
    leido= models.BooleanField()
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def clean(self):
        # Asegurarse de que el emisor y el receptor sean diferentes
        if self.emisor == self.receptor:
            raise ValidationError("El emisor y el receptor deben ser diferentes.")

    def __str__(self):
         return f'Comentario de {self.emisor} a {self.receptor} - {self.fechaComentario}'