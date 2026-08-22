from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tarefa = models.CharField(max_length=100)
    concluido = models.BooleanField(default=False)

