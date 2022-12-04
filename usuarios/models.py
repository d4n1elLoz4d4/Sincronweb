from django.utils.translation import gettext_lazy as _
from unittest.util import _MAX_LENGTH

# Create your models here.
class Usuario(models.Model):
    nombres=models.CharField(max_length=60, verbose_name="Nombres")
    apellidos=models.CharField(max_length=60, verbose_name="Apellidos")
    foto=models.ImageField(upload_to='images/usuarios',blank=True, default='images/usuarios/default.png')
    email= models.EmailField(max_length=150, verbose_name='Correo')

    class TipoDocumento(models.TextChoices):
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        TI='T.I', _('Tarjeta de Identidad')
        OT='Otro', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    documento=models.CharField(max_length=50, verbose_name="Número de Documento")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    fecha_nacimiento=models.DateField(verbose_name="Fecha de Nacimiento", help_text=u"MM/DD/AAAA")
   