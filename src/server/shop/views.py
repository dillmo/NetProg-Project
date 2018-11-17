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