from django.db import models

# Create your models here.
from django.db import models

from etapa1.models import Materie


class Teme_Materii(models.Model):

    nume_tema = models.CharField(max_length=100)
    nume_materie= models.ForeignKey(Materie, on_delete=models.CASCADE)
    text_tema= models.CharField(max_length=10000)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.nume_tema} {self.nume_materie}"