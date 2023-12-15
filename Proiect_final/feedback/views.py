from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.urls import reverse
from feedback.models import FeedbackCurs

class FeedbackView(ListView):
    model=FeedbackCurs
    template_name = 'feedback/feedback_form.html'
    context_object_name = 'lista_feedback'

class FeedbackCreateView(CreateView):
    model = FeedbackCurs
    template_name = 'forms.html'
    fields = ['nume_curs', 'profesor' , 'rating', 'comentarii']


    def get_success_url(self):
        return reverse('feedback:lista_feedback')
