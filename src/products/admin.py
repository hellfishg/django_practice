from django.contrib import admin

# Register your models here.
from .models import Product

# Mostrar en el backoffice el producto.
admin.site.register(Product)