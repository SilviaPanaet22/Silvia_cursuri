from django.urls import path

from et2 import views

app_name = 'et2'

urlpatterns = [
    path('', views.TEMEView.as_view(), name='lista_teme'),
    path('adaugare/', views.CreateTEME.as_view(), name='adaugare'),
    path('<int:pk>/modificare/', views.UpdateTEME.as_view(), name='modifica'),
    path('<int:pk>/dezactiveaza', views.deactivate_tema, name='dezactiveaza'),
    path('<int:pk>/activeaza', views.activate_tema, name='activeaza'),
    path('<int:pk>/stergere', views.delete_tema, name='stergere'),
]