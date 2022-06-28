from django.contrib.auth.models import User
from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    #imagen = models.FileField(upload_to='avatares', null=True, blank = True)
    imagen = models.FileField(upload_to='avatares', null=True, blank = True,)



class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.FileField(upload_to='avatares', null=True, blank = True)
    descripcion = models.CharField(max_length=1000)    
    autor = models.CharField(max_length=100)   
    
    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Autor" + self.autor
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()