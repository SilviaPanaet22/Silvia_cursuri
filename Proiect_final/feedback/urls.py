from django.urls import path

from feedback import views

app_name='feedback'

urlpatterns=[
    path('', views.FeedbackView.as_view(), name='lista_feedback'),
    path('adaugare/',views.FeedbackCreateView.as_view(), name='adaugare'),



]
