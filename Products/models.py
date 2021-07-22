from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(default=None)
    weight = models.IntegerField(default=None)
    price = models.IntegerField(default=None)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)

    def __str__(self):
        return self.name
