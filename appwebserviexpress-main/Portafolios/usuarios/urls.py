from django.urls import path
from . import views

app_name='usuarios'

urlpatterns = [
    path('register/',views.register, name='registro'),
    path('login/',views.login, name='inicio_sesion'),
    path('logout/',views.logout, name='cerrar_sesion'),    
    path('mensaje_registro/',views.mensaje_registro, name='mensaje_registro'),  
    path('modificar_perfil/<id>', views.modificar_perfil, name='modificar_perfil'),
]