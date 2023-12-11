from django.urls import path

from etapa2 import views

app_name='etapa2'
urlpatterns=[
    path('',views.TemeView.as_view(), name="lista_teme"),
    path('adaugare/',views.CreateTeme.as_view(), name='adaugare')

]