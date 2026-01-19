from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

def eliminar_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)

    # Solo el receptor puede eliminar el mensaje
    if mensaje.receptor != request.user:
        return render(request, 'mensajes/acceso_denegado.html')

    if request.method == 'POST':
        mensaje.delete()
        return redirect('mensajes:bandeja_entrada')

    # Si no es POST, mostrar confirmación
    return render(request, 'mensajes/confirmar_eliminacion.html', {'mensaje': mensaje})

def detalle_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    
    if mensaje.receptor != request.user and mensaje.remitente != request.user:
        return render(request, 'mensajes/acceso_denegado.html') 
    
    return render(request, 'mensajes/detalle_mensaje.html', {'mensaje': mensaje})


def bandeja_entrada(request):
    mensajes = Mensaje.objects.filter(receptor=request.user).order_by('-fecha')
    return render(request, 'mensajes/bandeja_entrada.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('mensajes:bandeja_entrada')
    else:
        form = MensajeForm()
    return render(request, 'mensajes/enviar_mensaje.html', {'form': form})
