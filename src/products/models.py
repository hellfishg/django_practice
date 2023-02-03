from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(auto_created=True)
    name = models.TextField(max_length=120, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=2, max_length=10000)
    summary = models.BooleanField(default=True)
