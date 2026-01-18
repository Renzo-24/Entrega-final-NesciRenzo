from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    biografia = models.TextField(blank=True)
    cumpleanos = models.DateField(null=True, blank=True)
    enlace = models.URLField(blank=True)

    def __str__(self):
        return f"{self.usuario.username} Perfil"

# Create your models here.
