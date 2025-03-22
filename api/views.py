from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    Proveedor_interno, Nombre_cambio, Valor_Cambio, 
    Cliente_fuera, Transacciones, Saldo, Venta
)
from .serializers import (
    Proveedor_internoSerializer, Nombre_cambioSerializer, Valor_CambioSerializer,
    Cliente_fueraSerializer, TransaccionesSerializer, SaldoSerializer, VentaSerializer
)

# API ViewSets
class Proveedor_internoViewSet(viewsets.ModelViewSet):
    queryset = Proveedor_interno.objects.all()
    serializer_class = Proveedor_internoSerializer
    permission_classes = [IsAuthenticated]

class Nombre_cambioViewSet(viewsets.ModelViewSet):
    queryset = Nombre_cambio.objects.all()
    serializer_class = Nombre_cambioSerializer
    permission_classes = [IsAuthenticated]

class Valor_CambioViewSet(viewsets.ModelViewSet):
    queryset = Valor_Cambio.objects.all()
    serializer_class = Valor_CambioSerializer
    permission_classes = [IsAuthenticated]

class Cliente_fueraViewSet(viewsets.ModelViewSet):
    queryset = Cliente_fuera.objects.all()
    serializer_class = Cliente_fueraSerializer
    permission_classes = [IsAuthenticated]

class TransaccionesViewSet(viewsets.ModelViewSet):
    queryset = Transacciones.objects.all()
    serializer_class = TransaccionesSerializer
    permission_classes = [IsAuthenticated]

class SaldoViewSet(viewsets.ModelViewSet):
    queryset = Saldo.objects.all()
    serializer_class = SaldoSerializer
    permission_classes = [IsAuthenticated]

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated]

