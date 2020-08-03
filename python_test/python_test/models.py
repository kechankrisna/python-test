# Insert models here
from django.db import models


class Client(models.Model):
    username = models.CharField("Name", max_length=30, unique=True, blank=True)
    contact_name = models.CharField("Contact Name", max_length=50, blank=True)
    email = models.CharField("Email", max_length=100, unique=True, blank=True)
    phone_number = models.CharField("Phone number", max_length=30, blank=True)
    street_name = models.CharField("Street name", max_length=50, blank=True)
    suburb = models.CharField("Suburb", max_length=50, unique=True, blank=True)
    postcode = models.CharField("Postcode", max_length=10, blank=True)
    state = models.CharField("State", max_length=50, blank=True)

    def __str__(self):
        return self.username
