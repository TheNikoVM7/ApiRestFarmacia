from django.db import models

# Create your models here.
class ProductosMedicos(models.Model):
    id_producto_medico = models.IntegerField(primary_key=True)
    nombre_producto_medico = models.CharField(max_length=50)
    stock_producto_medico = models.IntegerField()