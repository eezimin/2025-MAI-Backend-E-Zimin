from rest_framework import serializers
from .models import Product, Category, ProductCategory

# Сериализатор для категорий
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


# Сериализатор для связи продукта и категории
class ProductCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name', read_only=True)

    class Meta:
        model = ProductCategory
        fields = ['id', 'product', 'category', 'category_name']


# Сериализатор для продуктов
class ProductSerializer(serializers.ModelSerializer):
    categories = ProductCategorySerializer(
        source='productcategory_set', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'calories',
                  'protein', 'fat', 'carbs', 'categories']
