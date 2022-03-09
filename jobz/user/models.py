from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Person(AbstractBaseUser):
    name = models.CharField(max_length=500)
    cpf = models.BigIntegerField(primary_key=True)
    phone = models.BigIntegerField()
    email = models.EmailField(verbose_name="email", max_length=150, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDs = ['name', 'cpf']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perm(self, app_label):
        return True

class User(Person):
    # cpf = models.ForeignKey(Person, on_delete=models.CASCADE)
    pass

class Provider(Person):
    # idOcupation = models.ForeignKey()
    # cpf = models.ForeignKey(Person, on_delete=models.CASCADE)
    pass