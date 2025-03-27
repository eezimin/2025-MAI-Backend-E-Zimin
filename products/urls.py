from django.urls import path
from . import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api/profile/', views.profile, name='profile'),
    path('api/category/<str:category>/',
         views.category_page, name='category_page'),
    path('api/search/', views.search_products, name='search_products'),
    # path('api/products/', views.list_products, name='list_products'),
    path('api/products/create/', views.create_product, name='create_product'),

    # Продукты
    path('api/products/', views.ProductListCreateView.as_view(),
         name='product-list-create'),
    path('api/products/<int:pk>/',
         views.ProductDetailView.as_view(), name='product-detail'),

    # Категории
    path('api/categories/', views.CategoryListCreateView.as_view(),
         name='category-list-create'),
    path('api/categories/<int:pk>/',
         views.CategoryDetailView.as_view(), name='category-detail'),

    # Связь "продукт-категория"
    path('api/product-categories/', views.ProductCategoryListCreateView.as_view(),
         name='product-category-list-create'),
    path('api/product-categories/<int:pk>/',
         views.ProductCategoryDetailView.as_view(), name='product-category-detail'),

    path('api/docs/', include_docs_urls(title='Nutrition Tracker API')),

    path('web/products/', views.list_products, name='product-list'),
    # Детальная страница продукта
    path('web/products/<int:pk>/', views.product_detail, name='product-detail'),    
]
