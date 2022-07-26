# rest framework serializers
from rest_framework import serializers

#models

from .models import Raton, Teclado, Monitor, Computadora, Orden

class RatonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Raton
    fields = '__all__'


class TecladoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teclado
    fields = '__all__'


class MonitorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Monitor
    fields = '__all__'


class ComputadoraSerializer(serializers.ModelSerializer):
  class Meta:
    model = Computadora
    fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
  class Meta:
    model = Orden
    fields = '__all__'