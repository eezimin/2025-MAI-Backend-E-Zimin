from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Профиль пользователя
def profile(request):
    if request.method == "GET":
        return JsonResponse({"username": "user123", "email": "user@example.com"})


# Список продуктов
def product_list(request):
    if request.method == "GET":
        products = [
            {"id": 1, "name": "Apple", "calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 14},
            {"id": 2, "name": "Chicken Breast", "calories": 165, "protein": 31, "fat": 3.6, "carbs": 0},
        ]
        return JsonResponse(products, safe=False)

# Страница категории
def category_page(request, category):
    if request.method == "GET":
        return JsonResponse({"category": category, "products_count": 10})


@csrf_exempt  # Отключение CSRF-защиты для тестирования
def create_product(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            calories = data.get("calories")
            protein = data.get("protein")
            fat = data.get("fat")
            carbs = data.get("carbs")

            # Здесь можно добавить логику сохранения в базу данных
            return JsonResponse({
                "message": "Product created successfully",
                "product": {
                    "name": name,
                    "calories": calories,
                    "protein": protein,
                    "fat": fat,
                    "carbs": carbs,
                }
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid method"}, status=405)