from django import forms

from apps.empresa.models import Empresa

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa

        fields = [
            'nombre',
            'codigo',
            'descripcion',
        ]
        labels = {
            'nombre' : 'Nombre',
            'codigo' : 'Codigo',
            'descripcion' : 'Descripcion',
        }
        widgets = {
            'nombre' : forms.TextInput(),
            'codigo' : forms.TextInput(),
            'descripcion' : forms.TextInput(),
        }