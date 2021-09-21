"""examen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from examen.settings import STATICFILES_STORAGE
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView, logout_then_login

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('favicon.ico',RedirectView.as_view(url=staticfiles_storage.url('img/favicon.png'))),
    path('admin/', admin.site.urls),
    path('empresa/', include ('apps.empresa.urls')),
    path('departamento/', include ('apps.departamento.urls')),
    path('empleado/', include ('apps.empleado.urls')),
    path('administrador/', include ('apps.administrador.urls')),
    path('',LoginView.as_view(template_name='usuario/index.html')),
    path('accounts/login/',LoginView.as_view(template_name='usuario/index.html'),name='login'),
    path('logout/',logout_then_login,name='logout'),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
