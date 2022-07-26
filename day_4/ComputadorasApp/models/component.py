from django.db import models

# Create your models here.
class Component(models.Model):
    component = (
        ('Keyboard', 'Keyboard'),
        ('Mouse', 'Mouse'),
        ('Display', 'Display'),
        ('Speaker', 'Speaker'),
        ('Motherboard', 'Motherboard'),
        ('Processor', 'Processor')
    )
    type = models.CharField(choices=component, max_length=50)

    class Meta:
        abstract = True
    def __str__(self):
        return self.type

class Component(models.Model):
    type_component = models.CharField(max_length=50)
    def __str__(self):
      return self.type_component

class InputDevice(Component):
    mark = models.CharField(max_length=50)
    def __str__(self):
      return self.mark

class Keyboard(InputDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)
    def __str__(self):
      return str(self.quantity)

class Mouse(InputDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)
    def __str__(self):
      return str(self.quantity)

class OutputDevice(Component):
    mark = models.CharField(max_length=50)
    def __str__(self):
       return self.mark

class Display(OutputDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)
    def __str__(self):
      return str(self.quantity)

class Speaker(OutputDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)
    def __str__(self):
      return str(self.quantity)
