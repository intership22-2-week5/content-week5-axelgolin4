# rest framework serializers
from rest_framework import serializers

#models

from .models import Keyboard, Mouse, Display, Speaker, Computer, Order, OrderDetails

class KeyboardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Keyboard
    fields = '__all__'


class MouseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mouse
    fields = '__all__'


class DisplaySerializer(serializers.ModelSerializer):
  class Meta:
    model = Display
    fields = '__all__'


class SpeakerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Speaker
    fields = '__all__'

class ComputerSerializer(serializers.ModelSerializer):
    keyboard = serializers.PrimaryKeyRelatedField(queryset = Keyboard.objects.all())
    mouse = serializers.PrimaryKeyRelatedField(queryset = Mouse.objects.all())
    display = serializers.PrimaryKeyRelatedField(queryset = Display.objects.all())
    speaker = serializers.PrimaryKeyRelatedField(queryset = Speaker.objects.all())

    class Meta:
        model = Computer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # fields = '__all__'
        read_only_fields = ['total_cost']
        fields = ['id', 'code', 'created_at', 'updated_at', 'total_cost']


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        read_only_fields = ['total']
        fields = '__all__'