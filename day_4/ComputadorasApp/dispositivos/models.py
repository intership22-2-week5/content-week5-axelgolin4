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

class Computer(models.Model):
    name = models.CharField(max_length=50)
    display = models.ForeignKey(Display, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    quantity = models.IntegerField(null = True, blank = True)
    total_cost = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
      return self.name  

    def __str__(self):
        return f'{self.name}, stock: {self.quantity}'

    def decrement(self):
        keyboard = Keyboard.objects.filter(id=self.keyboard.id)[0]
        mouse = Mouse.objects.filter(id=self.mouse.id)[0]
        display = Display.objects.filter(id=self.display.id)[0]
        speaker = Speaker.objects.filter(id=self.speaker.id)[0]
        if keyboard.quantity >= self.quantity and mouse.quantity >= self.quantity and display.quantity >= self.quantity and speaker.quantity >= self.quantity:
            keyboard.quantity = self.keyboard.quantity - self.quantity
            mouse.quantity = self.mouse.quantity - self.quantity
            display.quantity = self.display.quantity- self.quantity
            speaker.quantity = self.speaker.quantity - self.quantity
            keyboard.save()
            mouse.save()
            display.save()
            speaker.save()
            self.total_cost = keyboard.cost + mouse.cost + display.cost + speaker.cost
            return True
        self.total_cost = 0
        return False
    def save(self, *args, **kwargs):
        if self.decrement():
            super(Computer, self).save(*args, **kwargs)
            return True
        return False

class Order(models.Model):
    total_cost = models.FloatField(null=True, blank=True)
    code = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order No. {self.id}'


class OrderDetails(models.Model):
    quantity = models.IntegerField(default=1)
    total = models.FloatField(blank=True, null=True)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, blank=True)
    orden = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'{self.orden} - {self.computer}'
        
    def decrement(self):
        if self.computer.quantity >= self.quantity:
            self.computer.quantity = self.computer.quantity - self.quantity
            self.computer.save()
            self.total = self.computer.total_cost * self.quantity
            self.orden.total_cost = self.orden.total_cost + self.total if self.orden.total_cost else self.total
            return True
        return False

    def save(self, *args, **kwargs):
        if self.decrement():
            super(OrderDetails, self).save(*args, **kwargs)
            return True
        return False
