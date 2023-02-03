from django.shortcuts import render
from django.http import HttpResponse

import os.path

# Create your views here.
def home_view(request, *arg, **kwargs):
    return render(request, "home.html", {})
  
def biblos_view(request, *arg, **kwargs):
    context_data = {
        "user" : "Anonimo",
        "age" : "23"
    }
    return render(request, "biblos.html", context_data)

def contac_view(request, *arg, **kwargs):
    return HttpResponse("<h1>PAGINA DE INICIO!</h1>")

