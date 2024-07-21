from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CapitalizeNameField(models.CharField):
    # Ensure valid values will always be using capitalize
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        return value if value is None else value.lower().capitalize()
    
class UpperNameField(models.CharField):
    # Ensure valid values will always be using just upper
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        return value if value is None else value.upper()

# Class Cuentas
class Cuenta(models.Model):
    
    nombre = CapitalizeNameField(max_length=50, unique=True)    
    
    def __str__(self):
        return f"{self.nombre}"
    

    class Meta:
        #verbose_name = _("")
        #verbose_name_plural = _("s")
        ordering = ['nombre']
             
"""
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
"""


# Class Monedas
class Moneda(models.Model):
    
    nombre = CapitalizeNameField(max_length=50, unique=True)
    sigla = models.CharField(max_length=3, unique=True)
    simbolo = models.CharField(max_length=1, unique=True)
    
    def __str__(self):
        return f"{self.nombre}"
    

    class Meta:
        #verbose_name = _("")
        #verbose_name_plural = _("s")
        ordering = ['nombre']
"""
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
"""
# Class Subcuentas
class Subcuenta(models.Model):
    
    TIPOS_CUENTAS = (
        ('INGRESO', 'Ingresos'),
        ('EGRESO', 'Egresos'),
        ('OTRO', 'Otro'),
    )
    
    nombre = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)
    tipo = models.CharField(choices=TIPOS_CUENTAS, default='OTRO', max_length=7)
    desc = models.TextField()
    moneda = models.ForeignKey('Moneda',on_delete=models.PROTECT)
    cuenta = models.ForeignKey('Cuenta',on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre}"
    
"""
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
"""

# Class Moviento, los movimientos que genero el asiento en las distintas cuentas
class Movimiento(models.Model):
    
    asiento = models.ForeignKey('Asiento', on_delete=models.CASCADE)
    monto = models.FloatField()
    cuenta = models.ForeignKey('Subcuenta', on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.asiento} - {self.monto}"
"""
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
"""

# Class Asiento contable
class Asiento(models.Model):
    
    fecha = models.DateField()
    usuario = models.ForeignKey(User, 
                                on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)
    desc = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.desc}"
    
    class Meta:
        #verbose_name = _("")
        #verbose_name_plural = _("s")
        ordering = ['fecha']
        
"""
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
"""


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    