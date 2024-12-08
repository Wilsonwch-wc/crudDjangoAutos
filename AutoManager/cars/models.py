from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now

# Validación personalizada para el precio
def validate_price(value):
    if value == 0 | value < 0:
        raise ValidationError('El precio debe ser mayor a 0.')

# Validación personalizada para el año
def validate_year(value):
    if value < 1886:  # Año del primer automóvil
        raise ValidationError('El año no puede ser anterior a 1886.')

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='autos')
    modelo = models.CharField(max_length=100)
    año = models.PositiveIntegerField(validators=[validate_year])
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price])
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='autos/', null=True, blank=True)

    def __str__(self):
        return f"{self.marca.nombre} {self.modelo} ({self.año})"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    auto = models.ForeignKey('Auto', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=now)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if Venta.objects.filter(auto=self.auto).exists():
            raise ValidationError('Este auto ya ha sido vendido.')

    def save(self, *args, **kwargs):
        self.clean()  # Llama a la validación personalizada antes de guardar
        super().save(*args, **kwargs)