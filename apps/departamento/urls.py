from django.urls import path,include
from apps.departamento.views import index
urlpatterns = [
    path(r'', index),
]