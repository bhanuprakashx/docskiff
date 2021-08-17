from django.db import models
from django.conf import settings

class User(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_name_1 = models.CharField(max_length= 30, default='')
    product_name_2 = models.CharField(max_length= 30, default='')
