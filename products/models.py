from django.db import models


class Category(models.Model):
    def __str__(self):
        return self.category_name
    category_name = models.CharField(max_length=255, default='Fruits')


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2038)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name


class Offer(models.Model):
    code = models.CharField(max_length=7)
    description = models.CharField(max_length=255)
    discount = models.FloatField(max_length=3)
    def __str__(self):
        return self.description





