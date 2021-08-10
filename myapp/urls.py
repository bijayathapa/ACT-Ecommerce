
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index, name="index"),
    path('store/',views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]