from django.urls import path, include
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/create/', login_required(views.ProductCreate.as_view()), name='create_product'),
    path('products/add/<int:pk>/', login_required(views.add_to_cart), name='add_to_cart'),
    path('products/add/<int:pk>/success/', views.product_added, name='product_added'),
    path('products/add/not_found/', views.product_not_found, name='product_not_found'),
    path('cart/', login_required(views.cart), name='cart'),
    path('checkout/', login_required(views.checkout), name='checkout'),
    path('checkout/success/', views.checkout_successful, name='checkout_successful'),
    path('api/', views.api, name='api'),
]