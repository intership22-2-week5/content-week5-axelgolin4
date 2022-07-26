#Django Rest Framework
from rest_framework.views import Response
from rest_framework import viewsets

# models
from .models import Autor, Foto, Obra, Exposicion

# serializers

from .serializers import AutorSerializer, FotoSerializer, ObraSerializer, ExposicionSerializer

class AutorViewSet(viewsets.ModelViewSet):
  queryset = Autor.objects.all()
  serializer_class = AutorSerializer

class FotoViewSet(viewsets.ModelViewSet):
  queryset = Foto.objects.all()
  serializer_class = FotoSerializer

class ObraViewSet(viewsets.ModelViewSet):
  queryset = Obra.objects.all()
  serializer_class = ObraSerializer

class ExposicionViewSet(viewsets.ModelViewSet):
  queryset = Exposicion.objects.all()
  serializer_class = ExposicionSerializer