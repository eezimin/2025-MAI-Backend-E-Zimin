from django.urls import path
from . import views

urlpatterns = [
    path('api/profile/', views.profile, name='profile'),
    path('api/products/', views.product_list, name='product_list'),
    path('api/category/<str:category>/', views.category_page, name='category_page'),
    path('api/create-product/', views.create_product, name='create_product'),
]