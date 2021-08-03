from django import forms

from apps.empleado.models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado

        fields = [
            'nombre',
            'fechaNacimiento',
            'curp',
            'empresa',
            'departamento',
            'correo',
            'sexo',
            'telefono',
            'celular',
        ]
        labels = {
            'nombre' : 'Nombre',
            'fechaNacimiento' : 'Fecha de Nacimiento',
            'curp' : 'CURP',
            'empresa' : 'Empresa',
            'departamento' : 'Departamento',
            'correo' : 'Correo',
            'sexo' : 'Genero',
            'telefono' : 'Telefono',
            'celular' : 'Celular',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'required': True}),
            'fechaNacimiento' : forms.DateInput(attrs={'type': 'date','class': 'datetimepicker'}),
            'curp' : forms.TextInput(attrs={'required': True}),
            'empresa' : forms.Select(attrs={'required': True}),
            'departamento' : forms.Select(attrs={'required': True}),
            'correo' : forms.TextInput(attrs={'required': True}),
            'sexo' : forms.Select(attrs={'required': True}),
            'telefono' : forms.TextInput(),
            'celular' : forms.TextInput(),
        }