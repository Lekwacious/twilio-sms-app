from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Shopper(models.Model):
    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=59)

    def __str__(self):
        return f"{self.name}"