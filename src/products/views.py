from django.shortcuts import render

from products.models import Product

# Create your views here.
def product_detail_view(request):
    context = { 'obj' : Product.objects.get(id=1) } # Creamos un diccionario con el objeto buscado.
    return render(request, "product_detail.html", context) # acepta diccionarios.
