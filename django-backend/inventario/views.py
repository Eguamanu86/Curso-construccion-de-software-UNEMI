from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Producto
from django.db.models import Q

class ProductoListView(LoginRequiredMixin, ListView):
    login_url = '/seguridad/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'inventario/productos.html'
    context_object_name = 'productos'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search', '')
        return Producto.objects.filter(
            Q(deleted=False),
            Q(codigo__icontains=search) |
            Q(nombre__icontains=search)
        )
