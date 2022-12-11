from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category ,on_delete=models.CASCADE)

    class Meta:
        db_table = "product"
        ordering = ("name","id")

    def __str__(self):
        return self.name