from django.shortcuts import render, redirect
from .models import Cliente, Auto, Marca, Venta
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Cliente, Auto, Venta,Marca
from .serializers import AutoSerializer, ClienteSerializer, MarcaSerializer, VentaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Auto
from .serializers import AutoSerializer
# Lista de clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()  # Obtenemos todos los clientes de la base de datos
    return render(request, 'cars/cliente_list.html', {'clientes': clientes})
def listar_marcas(request):
    marcas = Marca.objects.all()  # Obtenemos las marcas
    return render(request, 'cars/marca_list.html', {'marcas': marcas})

def registrar_marca(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        pais = request.POST['pais']
      
        Marca.objects.create(nombre=nombre, pais=pais)
        return redirect('listar_marca')
    return render(request, 'cars/marca_form.html')




# Lista de autos
def listar_autos(request):
    autos = Auto.objects.all()  # Obtenemos todos los autos de la base de datos
    return render(request, 'cars/auto_list.html', {'autos': autos})

# Lista de ventas
def listar_ventas(request):
    ventas = Venta.objects.all()  # Obtenemos todas las ventas de la base de datos
    return render(request, 'cars/venta_list.html', {'ventas': ventas})

# Registrar cliente
def registrar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        Cliente.objects.create(nombre=nombre, correo=correo, telefono=telefono)
        return redirect('listar_clientes')
    return render(request, 'cars/cliente_form.html')

# Registrar auto
def registrar_auto(request):
    if request.method == 'POST':
        marca = Marca.objects.get(id=request.POST['marca'])
        modelo = request.POST['modelo']
        año = request.POST['año']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        imagen = request.FILES.get('imagen')
        Auto.objects.create(marca=marca, modelo=modelo, año=año, precio=precio, descripcion=descripcion, imagen=imagen)
        return redirect('listar_autos')
    marcas = Marca.objects.all()
    return render(request, 'cars/auto_form.html', {'marcas': marcas})

# Registrar venta
def registrar_venta(request):
    if request.method == 'POST':
        cliente = Cliente.objects.get(id=request.POST['cliente'])
        auto = Auto.objects.get(id=request.POST['auto'])
        total = request.POST['total']
        Venta.objects.create(cliente=cliente, auto=auto, total=total)
        return redirect('listar_ventas')
    clientes = Cliente.objects.all()
    autos = Auto.objects.filter(venta__isnull=True)  # Mostrar solo autos no vendidos
    return render(request, 'cars/venta_form.html', {'clientes': clientes, 'autos': autos})



class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class AutoViewSet(ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VentaViewSet(ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
 


@api_view(['GET'])
def autos_disponibles(request):
    autos = Auto.objects.filter(venta__isnull=True)  # Autos que no tienen ventas asociadas
    serializer = AutoSerializer(autos, many=True)
    return Response(serializer.data)