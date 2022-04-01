from django.db import models


class Occupation(models.Model):
    occupation = models.CharField(max_length=25, unique=True, default='--',
        choices=(
            ('--', 'Categoria de Serviço'),
            ('Encanador', 'Encanador'),
            ('Diarista', 'Diarista'),
            ('Pedreiro', 'Pedreiro'),
            ('Tecnico', 'Tecnico')))