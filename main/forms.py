from django import forms
from .models import categoria, estadogestion, subcategoria

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