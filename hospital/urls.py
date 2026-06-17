
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('home/', views.home, name='home'),
    path('medicos/', include('apps.Medico.urls')),
    path('clientes/', include('apps.Cliente.urls')),
    path('citas/', include('apps.Cita.urls')),

]

