from django.contrib import admin
from .models import Product, Category, ProductCategory

# Регистрация модели Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'protein', 'fat',
                    'carbs')  # Поля для отображения в списке
    search_fields = ('name',)  # Поиск по названию продукта
    # Фильтры для списка продуктов
    list_filter = ('calories', 'protein', 'fat', 'carbs')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'category')
    list_filter = ('category',)
    search_fields = ('product__name', 'category__name')
