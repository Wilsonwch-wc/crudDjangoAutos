from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, AutoViewSet, ClienteViewSet, VentaViewSet, autos_disponibles

# Router para las vistas basadas en DRF
router = DefaultRouter()
router.register('marcas', MarcaViewSet)
router.register('autos', AutoViewSet)
router.register('clientes', ClienteViewSet)
router.register('ventas', VentaViewSet)

urlpatterns = [
    # Listas (vistas basadas en Django)
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('autos/', views.listar_autos, name='listar_autos'),
    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('marcas/', views.listar_marcas, name='listar_marcas'),

    # Formularios de registro
    path('clientes/registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('autos/registrar/', views.registrar_auto, name='registrar_auto'),
    path('ventas/registrar/', views.registrar_venta, name='registrar_venta'),
    path('marcas/registrar/', views.registrar_marca, name='registrar_marca'),

    # Endpoint personalizado
    path('api/autos-disponibles/', autos_disponibles, name='api_autos_disponibles'),
]

# Agregamos las rutas del router de DRF
urlpatterns += [
    path('api/', include(router.urls)),
]
