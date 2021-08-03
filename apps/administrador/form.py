from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:

        model = User
        fields = [
            'username',
            'is_staff'
        ]
        labels = {
            'username' : 'Nombre de Usuario',
            'is_staff' : 'Es Administrador Global ?',
        }