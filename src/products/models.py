from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True) # no es necesario declaralo. Django lo crea implicitamente.
    name = models.TextField(max_length=120, blank=False)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.BooleanField(default=True)
