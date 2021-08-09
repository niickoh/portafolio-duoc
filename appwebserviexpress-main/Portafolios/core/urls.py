from django.urls import path
from . import views

app_name ='core'

urlpatterns = [
   path('', views.index, name='index'),
   path('perfil/', views.perfil, name='perfil'),
   path('perfil/<str:username>/', views.perfil, name='perfil'),
   path('reservar_hora/', views.reserva_de_hora, name='reserva_de_hora'),
   path('listar_reserva/', views.listar_reserva_hora, name='listar_reserva'),
   path('listar_reserva/<str:username>/', views.listar_reserva_hora, name='listar_reserva'),
   path('modificar_reserva/<id>/', views.modificar_reserva, name='modificar'),
   path('eliminar_reserva/<id>/', views.eliminar_reserva, name='eliminar'),
   path('nuestros_servicios/', views.nuestros_servicios, name='servicios'),
   path('afinacion/', views.afinacion, name='afinacion'),
   path('aire_acondicionado/', views.aire_acondicionado, name='aire_acondicionado'),
   path('alineacion/', views.alineacion, name='alineacion'),
   path('banda_distribucion/', views.banda_de_distribucion, name='banda_distribucion'),
   path('bateria/', views.bateria, name='bateria'),
   path('bomba_agua/', views.bomba_agua, name='bomba_agua'),
   path('caja_transferencia/', views.caja_transferencia, name='caja_transferencia'),
   path('cambio_aceite/', views.cambio_aceite, name='cambio_aceite'),
   path('cambio_llantas/', views.cambio_llantas, name='cambio_llantas'),
   path('frenos/', views.frenos, name='frenos'),
   path('direccion_hidraulica/', views.direccion_hidraulica, name='direccion_hidraulica'),
   path('luces/', views.luces, name='luces'),
   path('boleta/<id>/', views.boleta, name='boleta'),
   path('mensaje_reserva/', views.mensaje_reserva, name='mensaje_reserva'),
   path('mensaje_mod_reserva/', views.mensaje_modificar_reserva, name='mensaje_modificar_reserva'),
]
