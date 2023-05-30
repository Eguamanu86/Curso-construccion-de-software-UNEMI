from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=10, blank=True, null=True)
    nombre = models.CharField(verbose_name="Categoria", max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de Producto'
        verbose_name_plural = 'Tipo de productos'


class Producto(models.Model):
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE,blank=True, null=True)
    codigo = models.CharField(verbose_name="Código", max_length=10, blank=True, null=True)
    nombre = models.CharField(verbose_name="nombre", max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
