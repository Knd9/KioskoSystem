from django.db import models

from django.db.models import DecimalField
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre