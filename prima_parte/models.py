# models.py
from django.db import models
from django.contrib.auth.models import User

class Retete_prajituri(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_reteta = models.TextField()
    timp_executie = models.IntegerField()  # timp în minute
    data_adaugare = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_adaugare']

    def __str__(self):
        return self.text_reteta
