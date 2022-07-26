from django.db import models
from component import Display, Speaker, Mouse, Keyboard
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
