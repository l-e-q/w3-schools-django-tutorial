from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_data = models.DateField(null=True)
