from django.db import models
from django.db.models import F

# Create your models here.
class DispositivoEntrada(models.Model):
  tipoEntrada = models.CharField(max_length=50) 
  marca = models.CharField(max_length=50)

class Raton(DispositivoEntrada):
  contadorRatones = models.IntegerField()

  def __str__(self):
    return f'{self.marca}'

class Teclado(DispositivoEntrada):
  contadorTeclados = models.IntegerField()
  def __str__(self):
    return f'{self.marca}'

class Monitor(models.Model):
  marca = models.CharField(max_length=50)
  tamaño = models.CharField(max_length=50)
  contadorMonitores = models.IntegerField()

  def __str__(self):
    return f'{self.marca}'

class Computadora(models.Model):
  nombre = models.CharField(max_length=50)
  monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
  teclado = models.ForeignKey(Teclado, on_delete=models.CASCADE)
  raton = models.ForeignKey(Raton, on_delete=models.CASCADE)
  contadorComputadora = models.IntegerField()

  def save(self, *args, **kwargs):
    '''
    REDUCION TECLADO RATON Y MONITOR
    '''
    Monitor.objects.filter(id=self.monitor.id).update(contadorMonitores=F('contadorMonitores') - 1)
    Raton.objects.filter(id = self.raton.id).update(contadorRatones = F('contadorRatones') - 1)
    Teclado.objects.filter(id = self.teclado.id).update(contadorTeclados = F('contadorTeclados') - 1)
    super(Computadora, self).save(*args, **kwargs)

  def __str__(self):
    return f'{self.nombre}'

class Orden(models.Model):
  computadoras = models.ManyToManyField(Computadora)
  contadorOrdenes = models.IntegerField()


  def __str__(self):
    return f'{self.marca}'
  