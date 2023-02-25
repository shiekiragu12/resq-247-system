from django.shortcuts import render
from .models import *


# Create your views here.

def list_product_view(request):
    context = {
        "products": Product.objects.all()
    }

    return render(request, template_name='shop/shop.html', context=context)


def cart(request):
    context = {}
    return render(request, template_name='shop/cart.html', context=context)


def checkout(request):
    context = {}
    return render(request, template_name='shop/checkout.html', context=context)

