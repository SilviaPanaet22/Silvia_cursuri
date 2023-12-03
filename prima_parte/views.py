from django.views.generic import ListView

from prima_parte.models import Retete_prajituri


class Retete_prajituriView(ListView):
    model=Retete_prajituri
    template_name = 'prima_parte/retete_index.html'

