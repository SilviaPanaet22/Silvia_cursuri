from django.db import models

# Create your models here.
class Materie(models.Model):
    nume = models.CharField(max_length=50)
    descriere = models.TextField(max_length=100)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at=models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.nume} {self.descriere}"

