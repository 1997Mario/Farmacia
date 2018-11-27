from django.contrib import admin
from .models import Compras, Cliente, Categoria, Venta, Laboratorio, Medicamento 
#Distribuidor,

# Register your models here.
admin.site.register(Compras)
admin.site.register(Cliente)
#admin.site.register(Distribuidor)
admin.site.register(Venta)
admin.site.register(Laboratorio)
admin.site.register(Medicamento)
admin.site.register(Categoria)
