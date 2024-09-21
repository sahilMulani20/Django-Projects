from django.db import models

# Create your models here.
class register(models.Model):
    objects = None
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email_id = models.CharField(max_length=25)
    password = models.CharField(max_length=15)
    rePassword = models.CharField(max_length=15)
    isTermsAgree = models.BooleanField()