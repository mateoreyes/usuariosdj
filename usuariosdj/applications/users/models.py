from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.



class User(AbstractBaseUser, PermissionsMixin):
    GENERO_CHOICES = (
        ('M','Masculino'),
        ('F', 'Femenino'),
        ('O','Otro'),
    )

    username = models.CharField(max_length=10,unique=True)
    email = models.EmailField(max_length=254)
    nombres = models.CharField (max_length=30, blank=True)
    apellidos = models.CharField (max_length=30,blank=True)
    genero = models.CharField(max_length=1,choices=GENERO_CHOICES,blank=True)
    # especificamos que el campo que sera utilizado para la autenticacion
    USERNAME_FIELD = 'username'