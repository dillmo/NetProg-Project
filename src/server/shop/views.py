from django.shortcuts import render
from django.http      import HttpResponse, HttpResponseRedirect
from django.urls      import reverse

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

def addToCart(request, product_id, color, size):
    return HttpResponse("cart")

def cart(request):
    context = {
        'product_id':   request.POST['product_id],
        'color':        request.POST['color'],
        'size':         request.POST['size']
    }
    return render(request, 'cart/index.html', context)
                                     
def checkout(request):
    context = {
        'name':         request.POST['name'],
        'email':        request.POST['email'],
        'phone':        request.POST['phone'],
        'address':      request.POST['address'],
        'apt_num':      request.POST['apt_num'],
        'zip':          request.POST['zip'],
        'city':         request.POST['city'],
        'state':        request.POST['state'],
        'country':      request.POST['country'],
        'card_num':     request.POST['card_num'],
        'exp_day':      request.POST['exp_day'],
        'exp_year':     request.POST['exp_year'],
        'cvt':          request.POST['cvt']
    }
    return render(request, 'checkout/index.html', context)
    
