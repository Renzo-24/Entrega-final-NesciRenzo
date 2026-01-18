from django.views.generic import TemplateView, ListView, DetailView
from .models import Pagina
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView



class InicioView(TemplateView):
    template_name = 'paginas/inicio.html'


class AcercaDeMiView(TemplateView):
    template_name = 'paginas/acerca_de_mi.html'


class ListaPaginasView(ListView):
    model = Pagina
    template_name = 'paginas/lista_paginas.html'
    context_object_name = 'paginas'


class DetallePaginaView(DetailView):
    model = Pagina
    template_name = 'paginas/detalle_pagina.html'


class CrearPaginaView(LoginRequiredMixin, CreateView):
    model = Pagina
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'paginas/crear_pagina.html'
    success_url = reverse_lazy('lista_paginas')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    
class EditarPaginaView(LoginRequiredMixin, UpdateView):
    model = Pagina
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'paginas/editar_pagina.html'
    success_url = reverse_lazy('lista_paginas')

class BorrarPaginaView(LoginRequiredMixin, DeleteView):
    model = Pagina
    template_name = 'paginas/borrar_pagina.html'
    success_url = reverse_lazy('lista_paginas')




