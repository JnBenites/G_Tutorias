from django.shortcuts import render, redirect
from disponibilidad.models import docente
from django.contrib.auth.models import User
# Create your views here.
#Dashboard
def panel_view(request):
    docentes = docente.objects.all()
    return render(request, 'base.html', {'docentes': docentes})

def usuario_view(request):
    users = User.objects.all()
    return render(request, 'usuario.html', {'users': users})

#def usuario_agregar_view(request):
#    users = User.objects.all()
#    return render(request, 'usuario_agregar.html', {'users': users})

def usuario_agregar_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario y usarlos con los campos correctos
        username  = request.POST.get('username')
        first_name = request.POST.get('nombre')
        email = request.POST.get('email')

        # Crear un nuevo usuario utilizando los campos first_name y email
        nuevo_usuario = User(username=username, first_name=first_name, email=email)
        nuevo_usuario.save()

        # Redirigir a la misma página después de agregar el usuario
        return redirect('usuario_agregar')

    # Si es una solicitud GET, simplemente mostrar el formulario y los usuarios existentes
    users = User.objects.all()  # Obtener todos los usuarios
    return render(request, 'usuario_agregar.html', {'users': users})