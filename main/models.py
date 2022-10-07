from django.db import models

class estadogestion(models.Model):
    idEstadoGestion = models.AutoField(primary_key=True)
    estadoGestionNombre = models.CharField(max_length= 45,verbose_name='Nombre')
    estadoGestionDescripcion = models.CharField(max_length= 125,verbose_name='Descripción')
    estadoGestionActivo = models.CharField(max_length= 1,verbose_name='Estado')

class categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    categoriaDescripcion = models.CharField(max_length= 45,verbose_name='Descripción')
    categoriaActivo = models.CharField(max_length= 1,verbose_name='Estado')


class subcategoria(models.Model):
    idSubcategoria = models.AutoField(primary_key=True)
    subcategoriaDescripcion = models.CharField(max_length= 45,verbose_name='Descripción')
    subcategoriaActivo = models.CharField(max_length= 1,verbose_name='Estado') 
    Categoria_idCategoria = models.IntegerField(verbose_name='Categoria')

class servicioOfrecido(models.Model):
    idServicioOfrecido = models.AutoField(primary_key=True)
    servicioOfrecidoNombre = models.CharField(max_length= 45,verbose_name='Nombre')
    servicioOfrecidoDesripcion = models.CharField(max_length= 125,verbose_name='Descripción')
    servicioOfrecidoActivo = models.CharField(max_length= 1,verbose_name='Estado') 
  