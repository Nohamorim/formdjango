from django.shortcuts import render, redirect
from .forms import ClienteForm

def home(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_usuarios')
    else:
        form = ClienteForm() 

    return render(request, 'usuarios/home.html', {'form': form})


def usuarios(request):
    pass