# rest framework serializers
from rest_framework import serializers

#models

from .models import Autor, Foto, Obra, Exposicion

class AutorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Autor
    fields = '__all__'


class FotoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Foto
    fields = '__all__'


class ObraSerializer(serializers.ModelSerializer):
  class Meta:
    model = Obra
    fields = '__all__'


class ExposicionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Exposicion
    fields = '__all__'