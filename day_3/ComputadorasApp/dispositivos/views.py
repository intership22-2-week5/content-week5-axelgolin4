#Django Rest Framework
from rest_framework.views import Response
from rest_framework import viewsets

# models
from .models import Raton, Teclado, Monitor, Computadora, Orden

# serializers

from .serializers import RatonSerializer, TecladoSerializer, MonitorSerializer, ComputadoraSerializer, OrdenSerializer

class RatonViewSet(viewsets.ModelViewSet):
  queryset = Raton.objects.all()
  serializer_class = RatonSerializer

class TecladoViewSet(viewsets.ModelViewSet):
  queryset = Teclado.objects.all()
  serializer_class = TecladoSerializer

class MonitorViewSet(viewsets.ModelViewSet):
  queryset = Monitor.objects.all()
  serializer_class = MonitorSerializer

class ComputadoraViewSet(viewsets.ModelViewSet):
  queryset = Computadora.objects.all()
  serializer_class = ComputadoraSerializer

class OrdenViewSet(viewsets.ModelViewSet):
  queryset = Orden.objects.all()
  serializer_class = OrdenSerializer