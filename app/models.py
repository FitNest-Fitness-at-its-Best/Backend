from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=50)
    profile_image = models.URLField(null=True, default=None)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'profile_image']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserHealthParam(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    height = models.FloatField()
    weight = models.FloatField()
    dob = models.DateTimeField()
    added_on = models.DateTimeField(auto_now_add=True)


class UserFoodLog(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serving = models.IntegerField()
    calories = models.FloatField(default=0.0)
    carbs = models.FloatField(default=0.0)
    proteins = models.FloatField(default=0.0)
    fats = models.FloatField(default=0.0)
    comments = models.TextField()
    edited = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)