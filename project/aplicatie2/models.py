

from django.db import models
from aplicatie1.models import Location




class Companies(models.Model):
    company_choices = (('SRL', 'S.R.L.'),
                       ('SA', 'S.A.'))

    name = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    company_type = models.CharField(max_length=5, choices=company_choices)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.company_type} {self.name}"