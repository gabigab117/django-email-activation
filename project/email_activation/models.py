from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, **kwargs):
        if not email:
            raise ValueError("Email must be set")
        if not first_name:
            raise ValueError("First name must be set")
        if not last_name:
            raise ValueError("Last name must be set")

        user = self.model(email=self.normalize_email(email), first_name=first_name,
                          last_name=last_name, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, first_name, last_name, password, **kwargs)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ["last_name", "first_name"]
    USERNAME_FIELD = "email"
    objects = CustomManager()
