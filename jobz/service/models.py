from django.db import models

class Services(models.Model):
	datePurchase = models.DateField()
	dateSevice = models.DateField()
	serviceDesription = models.CharField(max_length=5000)