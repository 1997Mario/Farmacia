from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre
    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('categoria-list')

class Compras(models.Model):
#distribuidor = models.CharField(max_length=50)
#producto = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    medicamento = models.ForeignKey('Medicamento', on_delete=models.PROTECT)
    def __str__(self):
        return self.cantidad+" "+self.medicamento

    def get_absolute_url(self):
        return reverse('compras-list')

"""class Distribuidor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    laboratorio = models.ForeignKey('Laboratorio', on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('distribuidor-list')"""

class Cliente(models.Model):
    
    documento = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('cliente-list')

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    autorizacion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('laboratorio-list')

class Medicamento(models.Model):
    medicamento = models.ImageField(upload_to='medicamento/')
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    concentracion = models.CharField(max_length=50) 
    componente = models.CharField(max_length=50)
    fecha_expedicion = models.CharField(max_length=50) 
    fecha_produccion = models.CharField(max_length=50)
    precio_compra = models.CharField(max_length=50)
    precio_venta = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('medicamento-list')

class Venta(models.Model):
    
    cliente = models.ForeignKey( 'Cliente',on_delete=models.PROTECT)
    medicamento = models.ForeignKey( 'Medicamento',on_delete=models.PROTECT)
    cantidad = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)

    def __str__(self):
        return self.cantidad+" "+self.valor

    def get_absolute_url(self):
        return reverse('venta-list')

@receiver(post_delete, sender=Medicamento)
def medicamento_delete(sender, instance, **kwargs):
    instance.medicamento.delete(False)