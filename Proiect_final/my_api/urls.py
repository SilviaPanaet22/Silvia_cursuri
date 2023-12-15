from rest_framework import routers
from my_api import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register('api', views.MaterieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]