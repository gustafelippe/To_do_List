from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('sucesso', views.sucesso, name='sucesso'),
    path('reset_pass', views.reset_pass, name='reset_pass'),
    path('reset_sucesso', views.reset_sucesso, name='reset_sucesso'),
]