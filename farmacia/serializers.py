from rest_framework import serializers
from .models import Cliente, Medicamento, Laboratorio, Venta, Compras, Categoria
#Distribuidor,

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')

class MedicamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medicamento
        fields = ('__all__')

class LaboratorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Laboratorio
        fields = ('__all__')

"""class DistribuidorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distribuidor
        fields = ('__all__')"""

class VentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venta
        fields = ('__all__')

class ComprasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compras
        fields = ('__all__')

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')