from django.db import models

# Create your models here.
from django.db import models

class FeedbackCurs(models.Model):
    nume_curs = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating de la 1 la 5
    comentarii = models.TextField(max_length=1000)

    def _str_(self):
        return f"{self.nume_curs} - {self.profesor}"