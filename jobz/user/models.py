from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from search.models import Occupation
from django.core.validators import MaxValueValidator, MinValueValidator

from .utils import validate_cpf

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
    name = models.CharField(
        validators=[RegexValidator(regex='^[a-zA-Z]{3}[a-zA-Z ]*$',
            message='Nome deve conter pelo menos 3 caracteres, apenas letras.',
            code='erro')],
        max_length=500,
        )
    cpf = models.CharField(
        max_length=11,
        primary_key=True,
        validators=[validate_cpf],
    )
    phone = models.BigIntegerField(
        validators=[
            MaxValueValidator(99999999999),
            MinValueValidator(11000000000),
        ],
    )
    email = models.EmailField(
        validators=[RegexValidator(regex='^[a-zA-Z0-9]{6,30}\@[a-z]{2,7}\.[a-z]{2,4}(\.[a-z]{2,4})?$',
            message='Email invalido.',
            code='erro')],
        verbose_name="email",
        max_length=150,
        unique=True)
    username = models.CharField(max_length=150, unique=False, verbose_name='username', null=True)
    password = models.CharField(
        max_length=128,
        validators=[RegexValidator(regex='^[a-zA-Z0-9+\-*^´+_)(&!@#]{8,128}$',
            message='Senha invalida. A senha deve conter mais de 8 digitos.',
            code='erro')],
        verbose_name='password',
        null=False,
        )

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
    occupation = models.ForeignKey(Occupation, null=True, on_delete=models.RESTRICT)