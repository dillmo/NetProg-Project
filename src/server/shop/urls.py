from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:product_id>', views.product, name='product'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('register/success', views.register_user, name='register_user'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('checkout/success', views.checkout_complete, name='checkout_complete')
]
