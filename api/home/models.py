from django.db import models


class Api(models.Model):
    name=models.CharField(max_length=20)
    product=models.CharField(max_length=20)
    desc=models.TextField(max_length=10)


