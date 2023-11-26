from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_patient = models.BooleanField('Is paitent', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)