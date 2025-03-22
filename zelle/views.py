from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from api.models import (
    Proveedor_interno, Nombre_cambio, Valor_Cambio, 
    Cliente_fuera, Transacciones, Saldo, Venta
)

# Proveedor_interno views
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'zelle/index.html'

# Proveedor_interno views
class Proveedor_internoListView(LoginRequiredMixin, TemplateView):
    template_name = 'zelle/proveedor_list.html'

class Proveedor_internoCreateView(LoginRequiredMixin, CreateView):
    model = Proveedor_interno
    template_name = 'zelle/proveedor_form.html'
    fields = ['nombre', 'celular', 'direccion', 'correo']
    success_url = reverse_lazy('proveedor-list')

class Proveedor_internoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proveedor_interno
    template_name = 'zelle/proveedor_form.html'
    fields = ['nombre', 'celular', 'direccion', 'correo']
    success_url = reverse_lazy('proveedor-list')

class Proveedor_internoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proveedor_interno
    template_name = 'zelle/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor-list')

# Nombre_cambio views
class Nombre_cambioListView(LoginRequiredMixin, TemplateView):
    template_name = 'zelle/nombre_cambio_list.html'

class Nombre_cambioCreateView(LoginRequiredMixin, CreateView):
    model = Nombre_cambio
    template_name = 'zelle/nombre_cambio_form.html'
    fields = ['nombre']
    success_url = reverse_lazy('nombre-cambio-list')

class Nombre_cambioUpdateView(LoginRequiredMixin, UpdateView):
    model = Nombre_cambio
    template_name = 'zelle/nombre_cambio_form.html'
    fields = ['nombre']
    success_url = reverse_lazy('nombre-cambio-list')

class Nombre_cambioDeleteView(LoginRequiredMixin, DeleteView):
    model = Nombre_cambio
    template_name = 'zelle/nombre_cambio_confirm_delete.html'
    success_url = reverse_lazy('nombre-cambio-list')

# Valor_Cambio views
class Valor_CambioListView(LoginRequiredMixin, TemplateView):
    template_name = 'zelle/valor_cambio_list.html'

class Valor_CambioCreateView(LoginRequiredMixin, CreateView):
    model = Valor_Cambio
    template_name = 'zelle/valor_cambio_form.html'
    fields = ['nombre', 'valor', 'fecha']
    success_url = reverse_lazy('valor-cambio-list')

class Valor_CambioUpdateView(LoginRequiredMixin, UpdateView):
    model = Valor_Cambio
    template_name = 'zelle/valor_cambio_form.html'
    fields = ['nombre', 'valor', 'fecha']
    success_url = reverse_lazy('valor-cambio-list')

class Valor_CambioDeleteView(LoginRequiredMixin, DeleteView):
    model = Valor_Cambio
    template_name = 'zelle/valor_cambio_confirm_delete.html'
    success_url = reverse_lazy('valor-cambio-list')

# Cliente_fuera views
class Cliente_fueraListView(LoginRequiredMixin, TemplateView):
    template_name = 'zelle/cliente_fuera_list.html'

class Cliente_fueraCreateView(LoginRequiredMixin, CreateView):
    model = Cliente_fuera
    template_name = 'zelle/cliente_fuera_form.html'
    fields = ['nombre', 'celular']
    success_url = reverse_lazy('cliente-fuera-list')

class Cliente_fueraUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente_fuera
    template_name = 'zelle/cliente_fuera_form.html'
    fields = ['nombre', 'celular']
    success_url = reverse_lazy('cliente-fuera-list')

class Cliente_fueraDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente_fuera
    template_name = 'zelle/cliente_fuera_confirm_delete.html'
    success_url = reverse_lazy('cliente-fuera-list')

# Transacciones views
class TransaccionesListView(LoginRequiredMixin, TemplateView):
    template_name = 'zelle/transacciones_list.html'

class TransaccionesCreateView(LoginRequiredMixin, CreateView):
    model = Transacciones
    template_name = 'zelle/transacciones_form.html'
    fields = ['nombre', 'valor']
    success_url = reverse_lazy('transacciones-list')

class TransaccionesUpdateView(LoginRequiredMixin, UpdateView):
    model = Transacciones
    template_name = 'zelle/transacciones_form.html'
    fields = ['nombre', 'valor']
    success_url = reverse_lazy('transacciones-list')

class TransaccionesDeleteView(LoginRequiredMixin, DeleteView):
    model = Transacciones
    template_name = 'zelle/transacciones_confirm_delete.html'
    success_url = reverse_lazy('transacciones-list')

# Saldo views
class SaldoListView(LoginRequiredMixin, TemplateView):
    template_name = 'zelle/saldo_list.html'

class SaldoCreateView(LoginRequiredMixin, CreateView):
    model = Saldo
    template_name = 'zelle/saldo_form.html'
    fields = ['nombre', 'valor']
    success_url = reverse_lazy('saldo-list')

class SaldoUpdateView(LoginRequiredMixin, UpdateView):
    model = Saldo
    template_name = 'zelle/saldo_form.html'
    fields = ['nombre', 'valor']
    success_url = reverse_lazy('saldo-list')

class SaldoDeleteView(LoginRequiredMixin, DeleteView):
    model = Saldo
    template_name = 'zelle/saldo_confirm_delete.html'
    success_url = reverse_lazy('saldo-list')

# Venta views
class VentaListView(LoginRequiredMixin, TemplateView):
    template_name = 'zelle/venta_list.html'

class VentaCreateView(LoginRequiredMixin, CreateView):
    model = Venta
    template_name = 'zelle/venta_form.html'
    fields = ['fecha', 'zelle', 'id_proveedor', 'destino', 'id_cambio', 'id_cliente_fuera', 'valor', 'saldo_restante']
    success_url = reverse_lazy('venta-list')

class VentaUpdateView(LoginRequiredMixin, UpdateView):
    model = Venta
    template_name = 'zelle/venta_form.html'
    fields = ['fecha', 'zelle', 'id_proveedor', 'destino', 'id_cambio', 'id_cliente_fuera', 'valor', 'saldo_restante']
    success_url = reverse_lazy('venta-list')

class VentaDeleteView(LoginRequiredMixin, DeleteView):
    model = Venta
    template_name = 'zelle/venta_confirm_delete.html'
    success_url = reverse_lazy('venta-list')

