
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('concluir/<int:tarefa_id>/', views.concluir, name='concluir'),
    path('excluir/<int:tarefa_id>/', views.excluir, name='excluir'),
]
