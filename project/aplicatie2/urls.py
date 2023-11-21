from django.urls import path
from aplicatie2 import views

app_name = 'aplicatie2'

urlpatterns =[
    path('', views.CompaniesView.as_view(), name='lista_companii'),
    path('adaugare/', views.CreateCompaniesView.as_view(), name='adaugare_c'),
    path('<int:pk>/modificare/', views.UpdateCompaniesView.as_view(), name='modifica'),
    path('<int:pk>/dezactiveaza', views.deactivate_company, name='dezactiveaza'),
    path('<int:pk>/activeaza', views.activate_company, name='activeaza'),
    path('<int:pk>/stergere', views.delete_company, name='stergere'),
]
