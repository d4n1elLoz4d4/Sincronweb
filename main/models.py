from django.db import models

class estadogestion(models.Model):
    idEstadoGestion = models.AutoField(primary_key=True)
    estadoGestionNombre = models.CharField(max_length= 45,verbose_name='Nombre')
    estadoGestionDescripcion = models.CharField(max_length= 125,verbose_name='Descripción')
    estadoGestionActivo = models.CharField(max_length= 1,verbose_name='Estado')
