"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# PYCHARM WARNING's
# Instalo django en el venv ni bien creo la carpeta del proyecto
# ANTES QUE NADA
# Acto seguido voy a File, Settings, Project, ProjectStructure y declaro
# la carpeta del prryecto como SOURCE folder, se pone en celeste en el árbol
# de proyecto. También lo puedo hacer con botón derecho sobre la carpeta y
# final  de la lista encuentro "Make Directory as" y selecciono SOURCE...


from django.contrib import admin
from django.urls import path
from proyecto1.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludando/', saludar),
    path('segundo/', segundavista),
    path('saludo/<nombre>', saludo_con_nombre),
    path('calculo/<edad>', calcula_anio_nacimiento),
    path('probandohtml/', probandohtml),
    path('probando2/', probando2),
]
