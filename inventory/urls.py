from .views import *
from django.urls import path

urlpatterns = [
    path('', sell_item, name='sell_item'), 
    path('inventory_list/', inventory_list, name='inventory_list'), 
    path('product/<int:pk>/', per_product_view, name='per_product'), 
    path('add_inventory/', add_product, name='add_inventory'),
    path('delete/<int:pk>/', delete_inventory, name='delete'), 
    path('update/<int:pk>/', update_inventory, name='update'), 
]

