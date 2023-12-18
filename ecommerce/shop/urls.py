from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('new/',views.CreateProduct.as_view(),name='create'),
    path('',views.ListProduct.as_view(),name='all'),
    path('detail/<int:pk>/',views.ProductDetail.as_view(),name='single'),
    path('category/<int:pk>/',views.CategoryProduct.as_view(),name="category_product"),
]


