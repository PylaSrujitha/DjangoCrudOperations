from django.core.validators import RegexValidator
from django.db import models

#
# Choices_branch=(('ece','ece'),('eee','eee'),('cse','cse'),('mech','mech'))
# Create your models here.
class Adminreg(models.Model):
    FirstName=models.CharField(max_length=200)
    LasttName=models.CharField(max_length=200)
    Username=models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    MobileNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    Email=models.EmailField(unique=True)
    branch=models.CharField(max_length=200)
    objects=models.manager


    class Meta:
        db_table='register_table'