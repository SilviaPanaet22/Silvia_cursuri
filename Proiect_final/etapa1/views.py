from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from etapa1.models import Materie
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
class MaterieView(ListView):
    model=Materie
    template_name = 'etapa1/materie_index.html'
    context_object_name = 'lista_materii'

class CreateMaterieView(CreateView):
    model=Materie
    fields = ['nume','descriere']
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('etapa1:lista_materii')
class UpdateMaterieView(LoginRequiredMixin,UpdateView):
    model = Materie
    fields = ['nume', 'descriere']
    template_name = 'forms.html'
    def get_success_url(self):
        return reverse('etapa1:lista_materii')


@login_required
def deactivate_materie(request, pk):
    Materie.objects.filter(id=pk).update(active=0)
    return redirect('etapa1:lista_materii')


@login_required
def activate_materie(request, pk):
    Materie.objects.filter(id=pk).update(active=1)
    return redirect('etapa1:lista_materii')


@login_required
def delete_materie(request, pk):
    Materie.objects.filter(id=pk).delete()
    return redirect('etapa1:lista_materii')

