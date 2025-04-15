from django.shortcuts import render, redirect
from myApp.forms import MeuFormulario, ClienteForm

def form_modelform(request):
    if request.method == "GET":
        form = ClienteForm()
        context = {
            'form': form
        }
        return render(request, 'formularios/formulario_modelform.html', context)
    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva direto no banco
            return redirect('form_modelform')  # Ou pode redirecionar pra outra página
        context = {
            'form': form
        }
        return render(request, 'formularios/formulario_modelform.html', context)
