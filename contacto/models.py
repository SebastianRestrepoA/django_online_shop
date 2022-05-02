from django.db import models

# Create your models here.

class Contacto(models.Model):

    asunto = models.CharField(max_length=50)
    correo = models.EmailField()
    mensaje = models.CharField(max_length=200)

