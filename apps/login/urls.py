from django.urls import path,include
from apps.login.views import index
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path(r'', index),
]