
from .views import inicio, mi_template, ver_fecha, saludo, mi_template, listado_usuarios
from django.urls import path

urlpatterns = [
    
    path('', inicio ),
    path('fecha/', ver_fecha ),
    path('saludo/<nombre>', saludo ),
    path('mi-template/<nombre_usuario>/<edad_usuario>', mi_template ),
    path('listado-usuarios/', listado_usuarios ),
]

