from django.shortcuts import render, get_list_or_404
from .models import Product
from django.http import HttpResponse

# Create your views here.
def index(request):
    products = get_list_or_404(Product)
    context = {"products":products}
    return render(request, "product/index.html", context)