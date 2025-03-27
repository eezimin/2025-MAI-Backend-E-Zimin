import factory
from django.contrib.auth.models import User
from .models import Product, Category, ProductCategory

# Фабрика для пользователей (если понадобится)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user_{n}")
    email = factory.Sequence(lambda n: f"user_{n}@example.com")
    password = factory.PostGenerationMethodCall('set_password', 'password123')

# Фабрика для категорий
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"Category {n}")

# Фабрика для продуктов
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f"Product {n}")
    calories = 52  # Фиксированное значение
    protein = 0.3   # Фиксированное значение
    fat = 0.2       # Фиксированное значение
    carbs = 14      # Фиксированное значение

# Фабрика для связи "продукт-категория"
class ProductCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductCategory

    product = factory.SubFactory(ProductFactory)
    category = factory.SubFactory(CategoryFactory)