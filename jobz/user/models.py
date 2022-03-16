from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Sobreescrever criação de user
class PersonManager(BaseUserManager):
    def _create_user(self, username, name, email, password, cpf, phone, is_staff, is_superuser):
        if not name:
            raise ValueError('Usuario deve possuir nome')
        email = self.normalize_email(email)
        user = self.model(username=username, name=name, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, cpf=cpf, phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, name, cpf, phone, email=None, password=None):
        return self._create_user(username, name, email, password, cpf, phone, False, False)

    def create_superuser(self,username, name, cpf, phone, email=None, password=None):
        user=self._create_user(username, name, email, password, cpf, phone, True, True)
        user.is_active=True
        user.save(using=self._db)
        return user

# Create your models here.
class Person(AbstractUser):
    name = models.CharField(max_length=500)
    cpf = models.BigIntegerField(primary_key=True)
    phone = models.BigIntegerField()
    email = models.EmailField(verbose_name="email", max_length=150, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = PersonManager()

    def __str__(self):
        return self.name

class User(Person):
    # cpf = models.ForeignKey(Person, on_delete=models.CASCADE)
    pass

class Provider(Person):
    # idOcupation = models.ForeignKey()
    # cpf = models.ForeignKey(Person, on_delete=models.CASCADE)
    pass