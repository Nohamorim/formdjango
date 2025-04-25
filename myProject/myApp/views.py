from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente

def home(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_usuarios')
    else:
        form = ClienteForm() 

    return render(request, 'usuarios/home.html', {'form': form})


def listagem_usuarios(request):
    listagem_usuarios = Cliente.objects.all()
    return render(request, 'usuarios/usuarios.html', {'listagem_usuarios': listagem_usuarios})