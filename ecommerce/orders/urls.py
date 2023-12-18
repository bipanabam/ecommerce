from django.urls import path

from . import views

app_name = "cart"

urlpatterns = [
    path('',views.CartView.as_view(),name='view_cart'),
    path('add/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:pk>/',views.CartItemDelete.as_view(),name='remove'),
    path('order/',views.place_order,name='order'),
    path('user/orders/',views.UserOrderList.as_view(),name='order_user'),
    path('order/<int:pk>/',views.OrderDetail.as_view(),name='order_detail')
]

