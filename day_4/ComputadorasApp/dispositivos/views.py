#Django Rest Framework
from rest_framework.views import Response
from rest_framework import viewsets

# models
from .models import Keyboard, Mouse, Display, Speaker, Computer, Order, OrderDetails

# serializers
from .serializers import KeyboardSerializer, MouseSerializer, DisplaySerializer, OrderDetailSerializer, SpeakerSerializer, ComputerSerializer, OrderDetailSerializer, OrderSerializer

class KeyboardViewSet(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer

class MouseViewSet(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer

class DisplayViewSet(viewsets.ModelViewSet):
    queryset = Display.objects.all()
    serializer_class = DisplaySerializer

class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.data['id']:
            return response
        return Response({ 'Mensaje': 'No hay stock' })

class OrderSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
 


class OrderDetailSet(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.data['id']:
            return response
        
        return Response({ 'message': 'Not enough stock' })   
