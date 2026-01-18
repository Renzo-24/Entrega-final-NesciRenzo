from django.urls import path
from .views import (
    InicioView,
    AcercaDeMiView,
    ListaPaginasView,
    DetallePaginaView,
    CrearPaginaView,
    EditarPaginaView,
    BorrarPaginaView,
)

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('about/', AcercaDeMiView.as_view(), name='acerca_de_mi'),
    path('pages/', ListaPaginasView.as_view(), name='lista_paginas'),
    path('pages/<int:pk>/', DetallePaginaView.as_view(), name='detalle_pagina'),
    path('pages/crear/', CrearPaginaView.as_view(), name='crear_pagina'),
    path('pages/<int:pk>/editar/', EditarPaginaView.as_view(), name='editar_pagina'),
    path('pages/<int:pk>/borrar/', BorrarPaginaView.as_view(), name='borrar_pagina'),
]