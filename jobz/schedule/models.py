from tkinter import CASCADE
from django.db import models
from user.models import Provider

class Schedule(models.Model):
    dayOfWeek = models.CharField(max_length=25, default='seg',
        choices=(
            ('seg', 'Segunda-Feira'),
            ('ter', 'Terça-Feira'),
            ('qua', 'Quarta-Feira'),
            ('qui', 'Quinta-Feira'),
            ('sex', 'Sexta-Feira'),
            ('sab', 'Sábado'),
            ('dom', 'Domingo')))
    entryTime = models.TimeField()
    endOfWork = models.TimeField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
