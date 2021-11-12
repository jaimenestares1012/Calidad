from django.db import models


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
class User(AbstractBaseUser, PermissionsMixin):
    username=models.CharField( max_length=40, unique=True)
    email=models.EmailField()
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD='username'

    REQUIRED_FIELDS=['email',]

    objects=UserManager()

    def get_short_name(self):
        return self.username 

    