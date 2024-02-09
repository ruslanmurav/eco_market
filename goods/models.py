from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='uploads/photos/category')


class Product(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='uploads/photos/products')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
