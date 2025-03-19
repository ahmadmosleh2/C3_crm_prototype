from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customer_list, name='customer_list'),
    path('products/', views.product_list, name='product_list'),
    path('sales/', views.sale_list, name='sale_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('products/add/', views.add_product, name='add_product'),
    path('sales/add/', views.add_sale, name='add_sale'),
]