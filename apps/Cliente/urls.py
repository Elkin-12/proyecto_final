from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_clientes, name='lista_clientes'),
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
]
