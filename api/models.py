from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)


class Item(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    income_date = models.DateField()


class Transfer(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    transfer_date = models.DateField()
