from django.urls import reverse
from django.views.generic import ListView,CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

from etapa2.models import Teme


# Create your views here.
class TemeView(LoginRequiredMixin, ListView):
    model = Teme
    template_name = 'etapa2/teme_index.html'

class CreateTeme(LoginRequiredMixin, CreateView):
    model= Teme
    fields=['titlu','materie', 'descriere']
    template_name='forms.html'

    def get_success_url(self):
        return reverse('etapa2.lista_teme')

