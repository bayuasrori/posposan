from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CustomerModel(models.Model):
    name = ""
    phone = ""
    email = ""
    country = ""
    city = ""
    address = ""


# Create your models here.
class SupplierModel(models.Model):
    name = ""
    phone = ""
    email = ""
    country = ""
    city = ""
    address = ""


class CustomUser(AbstractUser):

    is_owner = models.BooleanField(default=True)
    is_supplier = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=True)

    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-id']


# class RoleModel(models.Model):
#     name = models.CharField()
#     description = models.CharField()