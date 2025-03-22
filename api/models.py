from django.db import models


class Proveedor_interno(models.Model):
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre


class Nombre_cambio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Valor_Cambio(models.Model):
    nombre = models.ForeignKey(Nombre_cambio, on_delete=models.CASCADE, related_name='valores')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField()

    def __str__(self):
        return f"{self.nombre} - {self.valor} - {self.fecha}"


class Cliente_fuera(models.Model):
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Transacciones(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Saldo(models.Model):
    nombre = models.ForeignKey(Transacciones, on_delete=models.CASCADE, related_name='saldos')
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.valor}"


class Venta(models.Model):
    fecha = models.DateTimeField()
    zelle = models.DecimalField(max_digits=10, decimal_places=2)
    id_proveedor = models.ForeignKey(Proveedor_interno, on_delete=models.CASCADE, related_name='ventas')
    destino = models.CharField(max_length=100)
    id_cambio = models.ForeignKey(Valor_Cambio, on_delete=models.CASCADE, related_name='ventas')
    id_cliente_fuera = models.ForeignKey(Cliente_fuera, on_delete=models.CASCADE, related_name='ventas')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_restante = models.ForeignKey(Saldo, on_delete=models.CASCADE, related_name='ventas')

    def __str__(self):
        return f"Venta {self.id} - {self.fecha}"

