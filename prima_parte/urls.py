from django.urls import path
from prima_parte import views

urlpatterns = [
    path('adauga/', views.adauga_reteta, name='adauga_reteta'),
    path('edit/<int:pk>/', views.edit_reteta, name='edit_reteta'),
    path('sterge/<int:pk>/', views.sterge_reteta, name='sterge_reteta'),
    path('list/', views.reteta_list, name='reteta_list'),
]
