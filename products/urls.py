from django.urls import path
from . import views

urlpatterns = [
    path('api/profile/', views.profile, name='profile'),
    path('api/category/<str:category>/',
         views.category_page, name='category_page'),
    path('api/search/', views.search_products, name='search_products'),
    path('api/products/', views.list_products, name='list_products'),
    path('api/products/create/', views.create_product, name='create_product'),
]
