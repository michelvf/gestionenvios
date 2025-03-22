from django.urls import path
from .views import (
    Proveedor_internoListView, Nombre_cambioListView, Valor_CambioListView,
    Cliente_fueraListView, TransaccionesListView, SaldoListView, VentaListView,
    IndexView
)

urlpatterns = [
    # Rutas simplificadas que solo renderizan las plantillas
    path('', IndexView.as_view(), name='index'),
    path('proveedores/', Proveedor_internoListView.as_view(), name='proveedor-list'),
    path('nombres-cambio/', Nombre_cambioListView.as_view(), name='nombre-cambio-list'),
    path('valores-cambio/', Valor_CambioListView.as_view(), name='valor-cambio-list'),
    path('clientes-fuera/', Cliente_fueraListView.as_view(), name='cliente-fuera-list'),
    path('transacciones/', TransaccionesListView.as_view(), name='transacciones-list'),
    path('saldos/', SaldoListView.as_view(), name='saldo-list'),
    path('ventas/', VentaListView.as_view(), name='venta-list'),
]

