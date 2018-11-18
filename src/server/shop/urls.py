from django.urls import path, include

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/create/', views.ProductCreate.as_view(), name='create_product'),
]