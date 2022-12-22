from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import CartItem
# Create your views here.
def index(request):
    cart_items = CartItem.objects.filter(user=request.user)
    context = {"cart_items":cart_items}
    return render(request, "cart_item/cart.html", context)