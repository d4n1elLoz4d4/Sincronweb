from django import forms
from .models import categoria, estadogestion, subcategoria, servicioOfrecido

class EstadoGestionForms(forms.ModelForm):
    class Meta:
        model = estadogestion
        fields='__all__'

class categoriaForms(forms.ModelForm):
    class Meta:
        model = categoria
        fields='__all__'        

class subcategoriaForms(forms.ModelForm):
    class Meta:
        model = subcategoria
        fields='__all__'            

class servicioOfrecidoForms(forms.ModelForm):
    class Meta:
        model = servicioOfrecido
        fields='__all__'                    