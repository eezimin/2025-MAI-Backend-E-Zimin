from unittest.mock import patch, MagicMock
from django.test import TestCase, RequestFactory
from products.views import search_products
import json
from .factories import ProductFactory, CategoryFactory, ProductCategoryFactory


class SearchProductsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch('products.models.Product.objects.filter')  # Замена метода objects.filter на мок
    def test_search_products(self, mock_filter):
        # Создание мокированных продуктов
        mock_product_1 = MagicMock()
        mock_product_1.id = 1
        mock_product_1.name = "Apple"
        mock_product_1.calories = 52
        mock_product_1.protein = 0.3
        mock_product_1.fat = 0.2
        mock_product_1.carbs = 14
        mock_product_1.productcategory_set.all.return_value = [
            MagicMock(category=MagicMock(name="Fruits"))
        ]

        mock_product_2 = MagicMock()
        mock_product_2.id = 2
        mock_product_2.name = "Banana"
        mock_product_2.calories = 89
        mock_product_2.protein = 0.3
        mock_product_2.fat = 0.2
        mock_product_2.carbs = 14        
        mock_product_2.productcategory_set.all.return_value = [
            MagicMock(category=MagicMock(name="Fruits"))
        ]
        # Настройка мока
        mock_filter.return_value.distinct.return_value = [mock_product_1, mock_product_2]

        # Создание GET-запроса
        request = self.factory.get('/api/search/', {'q': 'apple'})
        print(f"Request method: {request.method}")
        print(f"Query parameter: {request.GET.get('q')}")        
        response = search_products(request)
        # Проверка результата
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        print(data)
        # Проверяем длину results
        self.assertEqual(len(data['results']), 0)

class SearchProductsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        # Создание тестовых данных через Factory Boy
        self.category_fruits = CategoryFactory(name="Fruits")

        # Явно указываем значения для продуктов
        self.product_apple = ProductFactory(
            name="Apple",
            calories=52,
            protein=0.3,
            fat=0.2,
            carbs=14
        )
        self.product_banana = ProductFactory(
            name="Banana",
            calories=89,
            protein=1.1,
            fat=0.3,
            carbs=23
        )

        # Создание связей между продуктами и категориями
        ProductCategoryFactory(product=self.product_apple, category=self.category_fruits)
        ProductCategoryFactory(product=self.product_banana, category=self.category_fruits)

    def test_search_products(self):
        # Создание GET-запроса
        request = self.factory.get('/api/search/', {'q': 'apple'})
        response = search_products(request)

        # Проверка результата
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['results']), 1)

        # Формируем ожидаемый результат
        expected_result = {
            'id': self.product_apple.id,
            'name': 'Apple',
            'calories': 52,
            'protein': 0.3,
            'fat': 0.2,
            'carbs': 14,
            'categories': ['Fruits']
        }

        # Проверяем содержимое results
        self.assertIn(expected_result, data['results'])