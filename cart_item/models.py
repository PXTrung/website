from django.db import models
from product.models import Product
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "cart_item"