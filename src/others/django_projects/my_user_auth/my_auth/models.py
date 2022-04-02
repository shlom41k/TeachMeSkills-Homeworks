from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name="Date of birth", null=True, blank=True)
    city = models.CharField(verbose_name="City", max_length=30, blank=True)

    # def __str__(self):
    #     return f"{self.__class__.username.__str__()}"