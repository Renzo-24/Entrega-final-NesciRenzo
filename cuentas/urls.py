from django.urls import path
from .views import ver_perfil, editar_perfil
from .views import (
    login_usuario,
    logout_usuario,
    registro_usuario,
)

urlpatterns = [
    path('login/', login_usuario, name='login'),
    path('logout/', logout_usuario, name='logout'),
    path('registro/', registro_usuario, name='registro'),
    path('perfil/', ver_perfil, name='ver_perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
]
