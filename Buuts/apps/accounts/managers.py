from rest_framework.authtoken.models import Token
#
from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):
    
    def _create_user(self, email, name, surnames, password, is_staff, is_superuser, is_active, is_employee, **extra_fields):
        user = self.model(
            email=email,
            name=name,
            surnames=surnames,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            is_employee=is_employee,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        #
        Token.objects.create(user=user)

        return user
    
    def create_user(self, email, name, surnames, password=None, **extra_fields):
        return self._create_user(email, name, surnames, password, False, False, False, False, **extra_fields)

    def create_superuser(self, email, name, surnames, password=None, **extra_fields):
        return self._create_user(email, name, surnames, password, True, True, True, False, **extra_fields)
