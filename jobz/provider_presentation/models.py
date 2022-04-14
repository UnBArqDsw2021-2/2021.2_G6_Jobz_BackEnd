from django.db import models
from user.models import Provider

class ProviderPresentation(models.Model):
    presentationPhoto = models.ImageField(upload_to='provider_presentation/images')
    description = models.CharField(max_length=5000)
    provider = models.ForeignKey(Provider, on_delete=models.RESTRICT)