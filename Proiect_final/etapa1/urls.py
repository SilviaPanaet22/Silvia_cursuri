from django.urls import path

from etapa1 import views

app_name='etapa1'

urlpatterns=[
    path('', views.MaterieView.as_view(), name='lista_materii'),
    path('adaugare/',views.CreateMaterieView.as_view(), name='adaugare'),

]