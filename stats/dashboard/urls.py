from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('staff/',views.staff,name='staff'),
    path('product/',views.product,name='product'),
    path('order/',views.order,name='order'),
    path('product/delete/<int:pk>/',views.product_delete,name='product-delete'),
    path('product/edit/<int:pk>/',views.product_edit,name='product-edit'),
    path('search/',views.search_product,name='search-product'),
]