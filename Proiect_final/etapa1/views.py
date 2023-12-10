from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView
from etapa1.models import Materie

class MaterieView(ListView):
    model=Materie
    template_name = 'etapa1/materie_index.html'

class CreateMaterieView(CreateView):
    model=Materie
    fields = ['nume','descriere']
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('etapa1:lista_materii')

