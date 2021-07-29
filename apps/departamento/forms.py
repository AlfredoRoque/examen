from django import forms

from apps.departamento.models import Departamento

class DepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento

        fields = [
            'nombre',
            'cod',
            'codigo',
        ]
        labels = {
            'nombre' : 'Nombre',
            'cod' : 'Codigo',
            'codigo' : 'Codigo Empresa',
        }
        widgets = {
            'nombre' : forms.TextInput(),
            'cod' : forms.TextInput(),
            'codigo' : forms.Select(attrs={'required': True}),
        }