from rest_framework import serializers
from .models import (
    Proveedor_interno, Nombre_cambio, Valor_Cambio, 
    Cliente_fuera, Transacciones, Saldo, Venta
)

class Proveedor_internoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor_interno
        fields = '__all__'

class Nombre_cambioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nombre_cambio
        fields = '__all__'

class Valor_CambioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valor_Cambio
        fields = '__all__'

class Cliente_fueraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente_fuera
        fields = '__all__'

class TransaccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacciones
        fields = '__all__'

class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saldo
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

