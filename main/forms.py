from django import forms
from .models import estadogestion

class EstadoGestionForms(forms.ModelForm):
    class Meta:
        model = estadogestion
        fields='__all__'