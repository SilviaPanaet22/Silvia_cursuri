from django.urls import path

from etapa1 import views

app_name='etapa1'

urlpatterns=[
    path('', views.MaterieView.as_view(), name='lista_materii'),
    path('adaugare/',views.CreateMaterieView.as_view(), name='adaugare'),
    path('<int:pk>/modifica/', views.UpdateMaterieView.as_view(), name='modifica'),
    path('<int:pk>/dezactiveaza', views.deactivate_materie, name='dezactiveaza'),
    path('<int:pk>/activeaza', views.activate_materie, name='activeaza'),
    path('<int:pk>/stergere', views.delete_materie, name='stergere'),


]
