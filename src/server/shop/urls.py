from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:product_id>', views.product, name='product'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]