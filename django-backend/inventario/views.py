from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Producto

class ProductoListView(LoginRequiredMixin, ListView):
    login_url = '/seguridad/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'inventario/productos.html'
    context_object_name = 'productos'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, **kwargs):
        return Producto.objects.filter(
            deleted=False
        )
