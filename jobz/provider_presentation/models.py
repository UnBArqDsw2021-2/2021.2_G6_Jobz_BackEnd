from django.db import models
from user.models import Provider

def nameFile(instance, filename):
    return "/".join(["images", str(instance.provider), filename])

class ProviderPresentation(models.Model):
    presentationPhoto = models.ImageField(upload_to=nameFile, blank=True, null=True)
    description = models.CharField(max_length=5000)
    provider = models.ForeignKey(Provider, on_delete=models.RESTRICT)