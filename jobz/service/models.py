from django.db import models
from user.models import User, Provider
from search.models import Occupation


class Services(models.Model):
    datePurchase = models.DateField(auto_now=True)
    dateService = models.DateField(null=False)
    serviceDescription = models.CharField(max_length=5000)
    user = models.ForeignKey(User, null=False, on_delete=models.RESTRICT)
    provider = models.ForeignKey(Provider, null=False, on_delete=models.RESTRICT)
