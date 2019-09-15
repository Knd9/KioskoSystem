from django.db import models

# Create your models here.
class Product(models.Model):
    codigo = models.CharField(max_length=100, unique=True, blank=True, null=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.nombre