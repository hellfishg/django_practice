from django.shortcuts import render

from products.models import Product
from products.forms import ProductForm

# Create your views here.
def product_detail_view(request):
    context = { 'obj' : Product.objects.get(id=1) } # Creamos un diccionario con el objeto buscado.
    return render(request, "product_detail.html", context) # acepta diccionarios.

# Creamos una pagina para la validacion y creacion de productos usando un "Controller"
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form': form
    }
    return render(request, "productForm.html", context)