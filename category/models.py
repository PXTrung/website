from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)

    class Meta:
        db_table = "category"
        ordering = ("name", "id")

    def __str__(self):
        return self.name