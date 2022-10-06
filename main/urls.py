from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('gestion/',views.estadogestionview,name='estadogestion'),
    path('gestion/nuevo',views.creareg,name='creaestado'),
    path('eliminar/<int:id>',views.eliminareg,name='eliminar'),
    path('gestion/editar/<int:id>',views.editarreg,name='editar')

]