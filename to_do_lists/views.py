from django.shortcuts import render
from .forms import TarefaForm
from .models import Tarefa


def index(request):
    
    if request.user.is_authenticated:
        tarefas_total = Tarefa.objects.filter(user=request.user)
        
        if tarefas_total is not None:
            tarefas_concluidas =[]
            tarefas_nao_concluidas = []
            
            for tarefa in tarefas_total:
                if tarefa.concluido == True:
                    tarefas_concluidas.append(tarefa)
                else:
                    tarefas_nao_concluidas.append(tarefa)
        else:
            tarefas_concluidas = None
            tarefas_nao_concluidas = None
            
            
        form = TarefaForm()
        context = {'form': form, 
                   'tarefas_concluidas': tarefas_concluidas, 
                   'tarefas_nao_concluidas': tarefas_nao_concluidas
                   }
        return render(request, 'to_do_lists/index.html', context)

    else:
        return render(request, 'to_do_lists/index.html')