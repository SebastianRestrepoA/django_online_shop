from django.contrib import admin
from inventario.models import Productos

# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display=('name', 'cost', 'cantidad_stock')
    search_fields = ('name', 'cost')

# admin.site.register(Productos)

admin.site.register(Productos, ProductosAdmin)