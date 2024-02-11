# myapp/views.py

from django.shortcuts import render, get_object_or_404
from .models import ProductMst, ProductSubCat

def product_manager(request):
    products = ProductMst.objects.all()
    return render(request, 'product_manager.html', {'products': products})

def product_details(request, product_id):
    product = get_object_or_404(ProductMst, pk=product_id)
    subcategories = ProductSubCat.objects.filter(product=product)
    return render(request, 'product_details.html', {'product': product, 'subcategories': subcategories})
