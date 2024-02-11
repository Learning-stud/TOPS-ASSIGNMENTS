
from django.urls import path
from . import views

urlpatterns = [
    path('product_manager/', views.product_manager, name='product_manager'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
]
