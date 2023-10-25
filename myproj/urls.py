
from django.urls import path
from django.contrib import admin
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
]
