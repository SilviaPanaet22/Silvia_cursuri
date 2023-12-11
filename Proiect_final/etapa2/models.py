from django.db import models

from etapa1.models import Materie


class Teme(models.Model):
    titlu = models.CharField(max_length=100)
    materie=models.ForeignKey(Materie,on_delete=models.CASCADE)
    descriere = models.TextField(max_length=200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.titlu} {self.materie} {self.descriere}"







