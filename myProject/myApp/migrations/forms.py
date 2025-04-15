from django import forms 

SEXO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino')
)

class MeuFormulario(forms.Form):...

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"