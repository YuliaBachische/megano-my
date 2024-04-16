from django.urls import path

from . import views

urlpatterns = [
    path("", views.cart_detail, name="cart_detail"),
    path("add/<int:product_seller_id>/", views.cart_add, name="cart_add"),
    path("remove/<int:product_seller_id>/", views.remove_cart, name="remove_cart"),
]
