from django.shortcuts import render

from apps.formularios.forms import MeuFormulario

def form_manual(request):

    context={}

    if request.method == "POST":

        erros = {}
        
        nome = request.POST.get['nome', None]
        sobrenome = request.POST.get['sobrenome', None]
        
    if nome != "Samuel":    
        erros['nome'] = "O nome não é o nome esperado"
    if sobrenome != "Gonçalves":
        erros['sobrenome'] = "O sobrenome não é o sobrenome esperado"

    if erros:
        context['erros'] = erros
        context['nome'] = nome
        context['sobrenome'] = sobrenome
    else:
        print("Salvando os dados")
        context['mensagem'] = "Os dados foram salvos com sucesso!"
            
    return render(request, 'formularios/formulario_manual.html', context=context)

def form_django(request):
    if request.method == "GET":
        form = MeuFormulario()
        context = {
            'form': form
        }
        return render(request, 'formularios/formulario_django.html', context)
    else:
        form = MeuFormulario(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form = MeuFormulario()
        context = {
                'form': form
        }
        return render(request, 'formularios/formulario_django.html', context)

def form_modelform(request):
    pass 
