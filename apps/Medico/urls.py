from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_medicos, name='lista_medicos'),
    path('registrar/', views.registrar_medico, name='registrar_medico'),
    path('especialidades/', views.lista_especialidades, name='lista_especialidades'),
    path('especialidades/registrar/', views.registrar_especialidad, name='registrar_especialidad'),
    path('eliminar/<int:medico_id>/', views.eliminar_medico, name='eliminar_medico'),
]