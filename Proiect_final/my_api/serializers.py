from rest_framework import serializers


from etapa1.models import Materie


class MaterieSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Materie
        fields = ['nume','descriere']