from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Product
from cart_item.models import CartItem
from django.http import HttpResponse
from pyexpat.errors import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    products = get_list_or_404(Product)
    context = {"products":products}
    return render(request, "product/index.html", context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    cart_item = CartItem.objects.filter(product=product, user=user).first()

    if cart_item is None:
        cart_item = CartItem()
        cart_item.product = product
        cart_item.quantity = 1
        cart_item.user = user
        cart_item.save()
    else:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(index)

#def sort_by_name(request):
    products = Product.object.all().order_by("name").values()
    context = {"products":products}
    return render(request, "product/index.html", context)

#def sort_by_price_asc(request):
    products = Product.objects.all().order_by("price").values()
    context = {"products":products}
    return render(request, "product/index.html", context)

#def sort_by_price_des(request):
    products = Product.objects.all().order_by("-price").values()
    context = {"products":products}
    return render(request, "product/index.html", context)
