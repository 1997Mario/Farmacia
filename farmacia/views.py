from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from farmacia.models import Categoria, Compras, Cliente, Venta, Laboratorio, Medicamento 
#Distribuidor,
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .serializers import CategoriaSerializer, ClienteSerializer, ComprasSerializer, VentaSerializer, LaboratorioSerializer, MedicamentoSerializer 
#DistribuidorSerializer,
from django.template import RequestContext as ctx

# Create your views here.

@login_required
def first_view(request):
    return render (request, 'base.html')

#Categoria
@login_required
def categoria(request):
    categoria_list= Categoria.objects.all()
    context = {'object_list': categoria_list}
    return render(request, 'farmacia/categoria.html', context)  

@login_required
def categoria_detail(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    context = {'object': categoria}
    return render(request, 'farmacia/categoria_detail.html', context)

@method_decorator(login_required, name='dispatch')
class categoriaUpdate(UpdateView):
    model=Categoria
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class categoriaCreate(CreateView):
    model=Categoria
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class categoriaDelete(DeleteView):
    model=Categoria
    success_url = reverse_lazy('categoria-list')
#Cliente
@method_decorator(login_required, name='dispatch')
class ClienteListView(ListView):
    model=Cliente
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ClienteDetailView(DetailView):
    model=Cliente
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ClienteUpdate(UpdateView):
    model=Cliente
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ClienteCreate(CreateView):
    model=Cliente
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ClienteDelete(DeleteView):
    model=Cliente
    success_url = reverse_lazy('cliente-list')

#Medicamento
@method_decorator(login_required, name='dispatch')
class MedicamentoListView(ListView):
    model=Medicamento
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class MedicamentoDetailView(DetailView):
    model=Medicamento
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class MedicamentoUpdate(UpdateView):
    model=Medicamento
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class MedicamentoCreate(CreateView):
    model=Medicamento
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class MedicamentoDelete(DeleteView):
    model=Medicamento
    success_url = reverse_lazy('medicamento-list')

#Compras
@method_decorator(login_required, name='dispatch')
class ComprasListView(ListView):
    model=Compras
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ComprasDetailView(DetailView):
    model=Compras
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ComprasUpdate(UpdateView):
    model=Compras
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ComprasCreate(CreateView):
    model=Compras
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ComprasDelete(DeleteView):
    model=Compras
    success_url = reverse_lazy('compras-list')

#Distribuidor
"""@method_decorator(login_required, name='dispatch')
class DistribuidorListView(ListView):
    model=Distribuidor
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class DistribuidorDetailView(DetailView):
    model=Distribuidor
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class DistribuidorUpdate(UpdateView):
    model=Distribuidor
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class DistribuidorCreate(CreateView):
    model=Distribuidor
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class DistribuidorDelete(DeleteView):
    model=Distribuidor
    success_url = reverse_lazy('distribuidor-list')"""

#Laboratorio
@method_decorator(login_required, name='dispatch')
class LaboratorioListView(ListView):
    model=Laboratorio
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class LaboratorioDetailView(DetailView):
    model=Laboratorio
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class LaboratorioUpdate(UpdateView):
    model=Laboratorio
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class LaboratorioCreate(CreateView):
    model=Laboratorio
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class LaboratorioDelete(DeleteView):
    model=Laboratorio
    success_url = reverse_lazy('laboratorio-list')

#Venta
@method_decorator(login_required, name='dispatch')
class VentaListView(ListView):
    model=Venta
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class VentaDetailView(DetailView):
    model=Venta
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class VentaUpdate(UpdateView):
    model=Venta
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class VentaCreate(CreateView):
    model=Venta
    fields = '__all__'

@method_decorator(login_required, name='dispatch')
class VentaDelete(DeleteView):
    model=Venta
    success_url = reverse_lazy('venta-list')

#Serializer
@method_decorator(login_required, name='dispatch')
class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

@method_decorator(login_required, name='dispatch')
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

@method_decorator(login_required, name='dispatch')
class ComprasViewSet(viewsets.ModelViewSet):
    queryset = Compras.objects.all()
    serializer_class = ComprasSerializer

@method_decorator(login_required, name='dispatch')
class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer

@method_decorator(login_required, name='dispatch')
class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

"""@method_decorator(login_required, name='dispatch')
class DistribuidorViewSet(viewsets.ModelViewSet):
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializer"""

@method_decorator(login_required, name='dispatch')
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
