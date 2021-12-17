from django.db import models
import string
import random


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Owner.objects.filter(code=code).count() == 0:
            break
    return code


class Owner(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    code = models.CharField(
        max_length=8, default=generate_unique_code, unique=True)


class Perishable(models.Model):
    code = models.CharField(
        max_length=8, default=generate_unique_code, unique=True)
    username = models.CharField(max_length=20, unique=False, default='DEFAULT')
    title = models.CharField(max_length=50, null=False)
    img_url = models.CharField(max_length=200, default=generate_unique_code)
    qty = models.IntegerField(null=False, default=1)
    rtr_date = models.DateField(auto_now_add=True)
    exp = models.DateField()
