from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),

    #Gestión
    path('gestion/',views.estadogestionview,name='estadogestion'),
    path('gestion/nuevo',views.creareg,name='creaestado'),
    path('eliminar/<int:id>',views.eliminareg,name='eliminar'),
    path('gestion/editar/<int:id>',views.editarreg,name='editar'),

    #Categoría
    path('categoria/',views.categoriaview,name='categoria'),
    path('categoria/nuevo',views.crearcategoria,name='creacategoria'),
    path('categoria/editar/<int:id>',views.editarCategoria,name='editarCategoria'),
    path('eliminarCategoria/<int:id>',views.eliminarCategoria,name='eliminarCategoria'),

    #SubCategoría
    path('subcategoria/',views.subcategoriaview,name='subcategoria'),
    path('subcategoria/nuevo',views.crearsubcategoria,name='creasubcategoria'),
    path('subcategoria/editar/<int:id>',views.editarsubCategoria,name='editarsubCategoria'),
    path('eliminarsubCategoria/<int:id>',views.eliminarsubCategoria,name='eliminarsubCategoria'),

    #ServicioOfrecido
    path('servicioOfrecido/',views.servicioOfrecidoview,name='servicioOfrecido'),
    path('servicioOfrecido/nuevo',views.crearservicioOfrecido,name='creaservicioOfrecido'),
    path('servicioOfrecido/editar/<int:id>',views.editarservicioOfrecido,name='editarservicioOfrecido'),
    path('eliminarservicioOfrecido/<int:id>',views.eliminarservicioOfrecido,name='eliminarservicioOfrecido')

    





]