from django.db import models


#su nombre, descripcion, precio sugerido de venta(debe ser positivo).
# Create your models here.
class Product(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.nombre