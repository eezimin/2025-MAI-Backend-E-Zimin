from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Category, ProductCategory
import json
from rest_framework import generics
from .serializers import ProductSerializer, CategorySerializer, ProductCategorySerializer


# Профиль пользователя
def profile(request):
    if request.method == "GET":
        return JsonResponse({"username": "user123", "email": "user@example.com"})


# Страница категории
def category_page(request, category):
    if request.method == "GET":
        return JsonResponse({"category": category, "products_count": 10})


def search_products(request):
    if request.method == "GET":
        query = request.GET.get("q", "").strip()
        if not query:
            return JsonResponse({"error": "Query parameter 'q' is required"}, status=400)

        # Ищем продукты по имени или категории
        products = Product.objects.filter(
            name__icontains=query
        ) | Product.objects.filter(
            productcategory__category__name__icontains=query
        )

        # Преобразуем результаты в JSON
        results = [
            {
                "id": product.id,
                "name": product.name,
                "calories": product.calories,
                "protein": product.protein,
                "fat": product.fat,
                "carbs": product.carbs,
                "categories": [pc.category.name for pc in product.productcategory_set.all()],
            }
            for product in products.distinct()
        ]

        return JsonResponse({"results": results})
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'products/product_detail.html', {'product': product})

# def list_products(request):
#     if request.method == "GET":
#         products = Product.objects.all()

#         # Преобразуем продукты в список словарей
#         results = [
#             {
#                 "id": product.id,
#                 "name": product.name,
#                 "calories": product.calories,
#                 "protein": product.protein,
#                 "fat": product.fat,
#                 "carbs": product.carbs,
#                 "categories": [pc.category.name for pc in product.productcategory_set.all()],
#             }
#             for product in products
#         ]

#         return JsonResponse({"products": results})
#     else:
#         return JsonResponse({"error": "Invalid method"}, status=405)


@csrf_exempt
def create_product(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            calories = data.get("calories")
            protein = data.get("protein")
            fat = data.get("fat")
            carbs = data.get("carbs")

            # Проверяем наличие обязательных полей
            if not all([name, calories, protein, fat, carbs]):
                return JsonResponse({"error": "All fields are required"}, status=400)

            # Создаем новый продукт
            product = Product.objects.create(
                name=name,
                calories=calories,
                protein=protein,
                fat=fat,
                carbs=carbs
            )

            return JsonResponse({
                "message": "Product created successfully",
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "calories": product.calories,
                    "protein": product.protein,
                    "fat": product.fat,
                    "carbs": product.carbs,
                }
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)



# Вьюшка для получения списка всех продуктов и создания нового продукта
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Вьюшка для получения детальной информации о продукте, обновления и удаления
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Вьюшка для получения списка всех категорий и создания новой категории
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Вьюшка для получения детальной информации о категории, обновления и удаления
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Вьюшка для получения списка всех связей "продукт-категория" и создания новой связи
class ProductCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

# Вьюшка для получения детальной информации о связи "продукт-категория", обновления и удаления
class ProductCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer