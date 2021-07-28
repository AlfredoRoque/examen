from django.urls import path,include
from apps.login.views import index
urlpatterns = [
    path(r'', index),
]