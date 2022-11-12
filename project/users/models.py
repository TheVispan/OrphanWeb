from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class CustomUser(AbstractUser, PermissionsMixin ):
    pass

    def __str__(self):
        return self.username