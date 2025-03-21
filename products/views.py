from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json


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
    if request.method == "GET":
        products = Product.objects.all()

        # Преобразуем продукты в список словарей
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
            for product in products
        ]

        return JsonResponse({"products": results})
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)


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
