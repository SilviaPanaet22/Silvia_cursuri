from rest_framework import viewsets



from etapa1.models import Materie
from my_api.serializers import MaterieSerializers, MaterieSerializers


# Create your views here.
class MaterieViewSet(viewsets.ModelViewSet):
    queryset = Materie.objects.all()
    serializer_class = MaterieSerializers




