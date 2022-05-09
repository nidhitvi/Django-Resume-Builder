from django.db import models
class user(models.Model):
    name=models.CharField(max_length=20, blank=False, null=False, primary_key=True)
    password=models.CharField(max_length=20,blank=False, null=False)
    mail=models.EmailField(null=False, blank=False)
    phone=models.ImageField(null=False, blank=False)
