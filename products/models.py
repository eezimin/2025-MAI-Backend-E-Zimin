from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()
    protein = models.FloatField()  # Белки
    fat = models.FloatField()      # Жиры
    carbs = models.FloatField()    # Углеводы

    def __str__(self):
        return self.name
