from django import forms
from myApp.models import Cliente  # Ajuste o caminho se estiver em outro lugar

SEXO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino')
)

class MeuFormulario(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    sobrenome = forms.CharField(label="Sobrenome", max_length=100)
    sexo = forms.ChoiceField(choices=SEXO_CHOICES, widget=forms.RadioSelect, required=False)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
