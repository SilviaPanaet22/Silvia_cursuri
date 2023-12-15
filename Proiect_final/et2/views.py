from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from et2.models import Teme_Materii


# Create your views here.
class TEMEView(LoginRequiredMixin, ListView):

    model = Teme_Materii
    template_name = 'et2/teme_index.html'
    context_object_name = 'lista_teme'


class CreateTEME(LoginRequiredMixin, CreateView):

    model = Teme_Materii
    fields = ['nume_tema', 'nume_materie', 'text_tema']
    template_name = 'forms.html'
    paginate_by = 10

    def get_success_url(self):
        return reverse('et2:lista_teme')


class UpdateTEME(LoginRequiredMixin, UpdateView):
    model = Teme_Materii
    fields = ['nume_tema', 'nume_materie', 'text_tema']
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('et2:lista_teme')

@login_required
def deactivate_tema(request, pk):
    Teme_Materii.objects.filter(id=pk).update(active=0)
    return redirect('et2:lista_teme')


@login_required
def activate_tema(request, pk):
    Teme_Materii.objects.filter(id=pk).update(active=1)
    return redirect('et2:lista_teme')


@login_required
def delete_tema(request, pk):
    Teme_Materii.objects.filter(id=pk).delete()
    return redirect('et2:lista_teme')

