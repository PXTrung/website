from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "profile"

    def __str__(self):
        return self.user.email