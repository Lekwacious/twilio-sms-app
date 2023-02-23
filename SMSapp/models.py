from django.db import models

class Shopper(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=59)

    def __str__(self):
        return f"{self.name}"