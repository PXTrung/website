from django.urls import path
from . import views

urlpatterns=[
     path("", views.index),
     path("delete/<int:id>",views.delete),
     path("increase_quantity/<int:id>", views.increase_quantity),
     path("decrease_quantity/<int:id>", views.decrease_quantity),
     path("update/<int:id>", views.update),
]