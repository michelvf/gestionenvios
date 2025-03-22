from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    Proveedor_internoViewSet, Nombre_cambioViewSet, Valor_CambioViewSet,
    Cliente_fueraViewSet, TransaccionesViewSet, SaldoViewSet, VentaViewSet
)

router = DefaultRouter()
router.register(r'proveedores', Proveedor_internoViewSet)
router.register(r'nombres-cambio', Nombre_cambioViewSet)
router.register(r'valores-cambio', Valor_CambioViewSet)
router.register(r'clientes-fuera', Cliente_fueraViewSet)
router.register(r'transacciones', TransaccionesViewSet)
router.register(r'saldos', SaldoViewSet)
router.register(r'ventas', VentaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

