
from django.urls import path
from . import views

app_name = 'mensajes'

urlpatterns = [
    path('', views.bandeja_entrada, name='bandeja_entrada'),
    path('enviar/', views.enviar_mensaje, name='enviar'),
    path('<int:pk>/', views.detalle_mensaje, name='detalle_mensaje'),
    path('<int:pk>/eliminar/', views.eliminar_mensaje, name='eliminar_mensaje'),
]
