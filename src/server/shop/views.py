from django.shortcuts import render
from django.http      import HttpResponse, HttpResponseRedirect
from django.urls      import reverse

my_cart = request.session.get('my_cart')

def index(request):
    context = {}
    return render(request, 'shop/index.html', context)

def product(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)

def login(request):
    return HttpResponse("login")

def register(request):
    context = {}
    return render(request, 'shop/register.html', context)

def register_user(request):
    context = {
        'email':    request.POST['email'],
        'username': request.POST['username'],
        'password': request.POST['password']
    }
    return HttpResponseRedirect(reverse('index'))

def addToCart(request, product_id):
    my_cart = request.session.push('my_cart', product_id)
    context = {}
    return render(request, 'shop/cart.html', context)

def cart(request):
    context = {
        'my_cart' = request.session.get('my_cart')
    }
    return HttpReponse("cart")
                              
def checkout(request):
    context = {}
    return render(request, 'shop/checkout/success.html', context)
    
