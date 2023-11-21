from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from aplicatie2.models import Companies


class CompaniesView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/list_companies.html'

class CreateCompaniesView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = ['name', 'company_type', 'location']
    template_name = 'forms2.html'
    def get_success_url(self):
        return reverse('aplicatie2:lista_companii')


class UpdateCompaniesView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = ['name', 'company_type', 'location']
    template_name = 'forms2.html'

    def get_success_url(self):
        return reverse('aplicatie2:lista_companii')


@login_required
def deactivate_company(request, pk):
    Companies.objects.filter(id=pk).update(status=0)
    return redirect('aplicatie2:lista_companii')


@login_required
def activate_company(request, pk):
    Companies.objects.filter(id=pk).update(status=1)
    return redirect('aplicatie2:lista_companii')


@login_required
def delete_company(request, pk):
    Companies.objects.filter(id=pk).delete()
    return redirect('aplicatie2:lista_companii')