from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.expressions import F
#
from .managers import UserManager
from .constants import *

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField('Name', max_length=50)
    surnames = models.CharField('Surnames', max_length=100)
    gender = models.CharField(
        'Gender',
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )
    date_birth = models.DateField(
        'Birth Date', 
        blank=True,
        null=True
    )
    phone = models.CharField('Phone', max_length=15, blank=True)
    adress = models.CharField('Addres', max_length=300, blank=True)
    cp = models.CharField('C.P', max_length=10, blank=True)
    city = models.CharField('City', max_length=50, blank=True)
    country = models.CharField('Country', max_length=50, blank=True)

    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    #
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surnames']

    objects = UserManager()


    def get_full_name(self):
        return self.name + ' ' + self.surnames

    def __str__(self):
        return str(self.id) + ' - ' + self.email
    