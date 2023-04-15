from django.db import models

# Create your models here.
from django.db import models

class Register(models.Model):

    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=10)

    def __str__(self):
        return self.nome