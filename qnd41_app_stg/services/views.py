from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Service_Product
from cart.forms import CartAddProductForm, CartAddServiceForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'services/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'services/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

def produc_servicest_detail(request, id, slug):
    service = get_object_or_404(Service_Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_service_product_form = CartAddServiceForm()
    return render(request,
                  'services/product/services_detail.html',
                  {'service': service,
                   'cart_service_product_form': cart_service_product_form})

