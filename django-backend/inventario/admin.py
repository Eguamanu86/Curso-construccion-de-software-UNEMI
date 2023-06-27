from django.contrib import admin
from .models import *

# Register your models here.
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'nombre',
        'estado'
    )
    list_per_page = 10
    search_fields = ('codigo','nombre')
    list_filter = (
        'estado',
    )

admin.site.register(TipoProducto,TipoProductoAdmin)


class ProductoAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Datos del producto', {
            'fields': [
                ('codigo',),
                ('nombre', 'tipo_producto'),
                ('pvp',)
            ]
        }),
        ('Stock del producto', {
            'fields': [
                ('stock_minimo','stock_maximo'),
                ('stock_disponible',)
            ]
        })
    ]

    list_display = (
        'codigo',
        'nombre',
        'tipo_producto',
        'stock_disponible',
        'pvp',
        'estado'
    )
    list_per_page = 20
    search_fields = ('codigo','nombre')
    list_filter = (
        'tipo_producto',
        'estado',
    )
admin.site.register(Producto, ProductoAdmin)
