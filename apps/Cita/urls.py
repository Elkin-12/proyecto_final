from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_citas, name='lista_citas'),
    path('registrar/', views.registrar_cita, name='registrar_cita'),
    path('servicios/', views.lista_servicios, name='lista_servicios'),
    path('servicios/eliminar/<int:servicio_id>/', views.eliminar_servicio, name='eliminar_servicio'),
    path('editar/<int:cita_id>/', views.editar_cita, name='editar_cita'),
    path('cambiar-estado/<int:cita_id>/<str:estado>/', views.cambiar_estado_cita, name='cambiar_estado_cita'),
    path('eliminar/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),
]
