from  django.contrib import messages
from django.shortcuts import render,redirect, get_list_or_404, get_object_or_404
from .models import CartItem
# Create your views here.
def index(request):
    cart_items = CartItem.objects.filter(user=request.user)
    context = {"cart_items":cart_items}
    return render(request, "cart_item/cart.html", context)

def delete(request, id):
    item = get_object_or_404(CartItem, id=id)
    item.delete()
    messages.success(request, ("Delete successfully"))
    return redirect(index)

def update(request, id):
    item = get_object_or_404(CartItem, id=id)
    item.quantity = request.POST["quantity"]
    item.save()

    messages.success(request, ("Update quantity successfully"))
    return redirect(index)

def increase_quantity(request, id):
    item = get_object_or_404(CartItem, id=id)
    item.quantity +=1
    item.save()
    return redirect(index)

def decrease_quantity(request, id):
    item = get_object_or_404(CartItem, id=id)
    item.quantity -= 1
    item.save()
    return redirect(index)