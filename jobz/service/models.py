from django.db import models
from user.models import User, Provider
from search.models import Occupation

class Services(models.Model):
	datePurchase = models.DateField(auto_now=True)
	dateService = models.DateField()
	serviceDescription = models.CharField(max_length=5000)
	user = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
	provider = models.ForeignKey(Provider, null=True, on_delete=models.RESTRICT)
	occupation = models.ForeignKey(Occupation, null=True, on_delete=models.RESTRICT)