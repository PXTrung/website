from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("add_cart/<int:product_id>", views.add_to_cart)
]

