from django.contrib import admin
from .models import Marca, Auto,Cliente,Venta

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'año', 'precio')
    search_fields = ('modelo', 'marca__nombre')
    list_filter = ('marca', 'año')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono')  # Campos que quieres mostrar en el admin
    search_fields = ('nombre', 'correo')  # Habilita búsqueda por nombre y correo

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'auto', 'fecha', 'total')
    search_fields = ('cliente__nombre', 'auto__modelo')
    list_filter = ('fecha',)