from django.shortcuts import render, redirect
from django.http      import HttpResponse
from django.urls      import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def index(request):
    context = {}
    return render(request, 'shop/index.html', context)

def product(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)

# From https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('shop:index')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})