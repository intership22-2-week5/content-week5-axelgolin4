from pydoc import describe
from django.db import models

# Create your models here.

class Autor(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'


class Foto(models.Model):
  name = models.CharField(max_length=50)
  date = models.DateField()
  uri = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.name}'
  
class Obra(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=50)
  price = models.IntegerField()
  photo = models.ManyToManyField(Foto)
  author = models.ManyToManyField(Autor)


  def __str__(self):
    return f'{self.name}'

class Exposicion(models.Model):
  titulo = models.CharField(max_length=50)
  fecha = models.CharField(max_length=200)
  lugar = models.CharField(max_length=13)
  Descripcion = models.BooleanField(default=True)
  Obra = models.ManyToManyField(Obra)
 
  def __str__(self):
    return f'{self.titulo}'