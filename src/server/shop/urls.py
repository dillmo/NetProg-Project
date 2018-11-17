from django.urls import path, include

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:product_id>', views.product, name='product'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]