from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='product'),
    path("add_cart/<int:product_id>", views.add_to_cart),
    #path("sort_by_name", views.sort_by_name),
    #path("sort_by_price_asc", views.sort_by_price_asc),
    #path("sort_by_price_des", views.sort_by_price_des)
]

