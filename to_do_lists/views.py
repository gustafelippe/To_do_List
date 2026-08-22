from django.shortcuts import render
from .forms import TarefaForm

def index(request):
    
    form = TarefaForm()
    context = {'form': form}
    return render(request, 'to_do_lists/index.html', context)
