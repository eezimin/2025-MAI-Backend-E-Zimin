from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()
    protein = models.FloatField()  # Белки
    fat = models.FloatField()      # Жиры
    carbs = models.FloatField()    # Углеводы

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} - {self.category}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_products = models.ManyToManyField(Product, related_name='favorited_by')

    def __str__(self):
        return self.user.username