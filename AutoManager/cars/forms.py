from django import forms
from .models import Cliente, Auto, Venta,Marca

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        }

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'año', 'precio', 'descripcion', 'imagen']
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo del auto'}),
            'año': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'auto', 'fecha', 'total']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'auto': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total'}),
        }

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'pais']
        widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la marca'}),
            'pais': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Pais de la marca'}),
   
        }
