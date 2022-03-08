from statistics import mode
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=500)
    cpf = models.BigIntegerField(primary_key=True)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=150)

class User(Person):
    # cpf = models.ForeignKey(Person, on_delete=models.CASCADE)
    pass

class Provider(Person):
    # idOcupation = models.ForeignKey()
    # cpf = models.ForeignKey(Person, on_delete=models.CASCADE)
    pass