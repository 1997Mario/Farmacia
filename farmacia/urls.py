from django.contrib import admin
from django.urls import include, path
from farmacia import views
from rest_framework import routers

router= routers.DefaultRouter()
router.register('compras_rest', views.ComprasViewSet)
router.register('cliente_rest', views.ClienteViewSet)
router.register('categoria_rest', views.CategoriaViewSet)
router.register('medicamento_rest', views.MedicamentoViewSet)
router.register('laboratorio_rest', views.LaboratorioViewSet)
router.register('venta_rest', views.VentaViewSet)

urlpatterns = [
    path('api/', include (router.urls)),

    path('', views.first_view, name='base'),
    #Cliente
    path('cliente/', views.ClienteListView.as_view(), name='cliente-list'),
    path('cliente/<int:pk>/detail/', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('cliente/<int:pk>/update/',views.ClienteUpdate.as_view(), name='cliente-update'),
    path('cliente/create/', views.ClienteCreate.as_view(), name='cliente-create'),
    path('cliente/<int:pk>/', views.ClienteDelete.as_view(), name='cliente-delete'),

    #Medicamento
    path('medicamento/', views.MedicamentoListView.as_view(), name='medicamento-list'),
    path('medicamento/<int:pk>/detail/', views.MedicamentoDetailView.as_view(), name='medicamento-detail'),
    path('medicamento/<int:pk>/update/',views.MedicamentoUpdate.as_view(), name='medicamento-update'),
    path('medicamento/create/', views.MedicamentoCreate.as_view(), name='medicamento-create'),
    path('medicamento/<int:pk>/', views.MedicamentoDelete.as_view(), name='medicamento-delete'),

    #Compras
    path('compras/', views.ComprasListView.as_view(), name='compras-list'),
    path('compras/<int:pk>/detail/', views.ComprasDetailView.as_view(), name='compras-detail'),
    path('compras/<int:pk>/update/',views.ComprasUpdate.as_view(), name='compras-update'),
    path('compras/create/', views.ComprasCreate.as_view(), name='compras-create'),
    path('compras/<int:pk>/', views.ComprasDelete.as_view(), name='comrpas-delete'),

    #Categoria
    path('categoria/', views.categoria, name='categoria-list'),
    path('categoria/<int:pk>/detail/', views.categoria_detail, name='categoria-detail'),
    path('categoria/<int:pk>/update/', views.categoriaUpdate.as_view(), name='categoria-update'),
    path('categoria/create/', views.categoriaCreate.as_view(), name='categoria-create'),
    path('categoria/<int:pk>/delete/', views.categoriaDelete.as_view(), name='categoria-delete'),
   
    #Laboratorio
    path('laboratorio/', views.LaboratorioListView.as_view(), name='laboratorio-list'),
    path('laboratorio/<int:pk>/detail/', views.LaboratorioDetailView.as_view(), name='laboratorio-detail'),
    path('laboratorio/<int:pk>/update/',views.LaboratorioUpdate.as_view(), name='laboratorio-update'),
    path('laboratorio/create/', views.LaboratorioCreate.as_view(), name='laboratorio-create'),
    path('laboratorio/<int:pk>/', views.LaboratorioDelete.as_view(), name='laboratorio-delete'),

        #Laboratorio
    path('venta/', views.VentaListView.as_view(), name='venta-list'),
    path('venta/<int:pk>/detail/', views.VentaDetailView.as_view(), name='venta-detail'),
    path('venta/<int:pk>/update/',views.VentaUpdate.as_view(), name='venta-update'),
    path('venta/create/', views.VentaCreate.as_view(), name='venta-create'),
    path('venta/<int:pk>/', views.VentaDelete.as_view(), name='venta-delete'),
]
