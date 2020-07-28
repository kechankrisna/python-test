# Insert models here
from django.db import models


class Client(models.Model):
    username = models.CharField("Name", max_length=30, unique=True, null=True)
    contact_name = models.CharField("Contact Name", max_length=50, null=True)
    email = models.CharField("Email", max_length=100, unique=True)
    phone_number = models.CharField("Phone number", max_length=30, null=True)
    street_name = models.CharField("Street name", max_length=50, null=True)
    suburb = models.CharField("Suburb", max_length=50, null=True, unique=True)
    postcode = models.CharField("Postcode", max_length=10, null=True)
    state = models.CharField("State", max_length=50, null=True)

    def __str__(self):
        return self.username
