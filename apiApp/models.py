from django.db import models

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

class Product(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # Rasim uchun maydon
