from django import forms

class TarefaForm(forms.Form):

    tarefa = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'id' : 'id_tarefa',
            'class': 'form-control', 
            'placeholder': 'Digite sua tarefa aqui...',
        }))
    