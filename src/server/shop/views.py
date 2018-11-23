from django.shortcuts            import render, redirect
from django.http                 import HttpResponse
from django.urls                 import reverse_lazy
from django.contrib.auth.forms   import UserCreationForm
from django.contrib.auth         import login, authenticate
from django.views.generic.edit   import CreateView
from django.views.generic.list   import ListView
from django.views.generic.detail import DetailView
from shop.models                 import Product
from django.utils                import timezone

class ProductListView(ListView):
    model = Product
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def add_to_cart(request, pk):
    if Product.objects.filter(pk=pk).exists():
        cart = request.session.get('cart', [])
        if Product.objects.get(pk=pk).stock > cart.count(pk):
            cart.append(pk)
            request.session['cart'] = cart
            return redirect('shop:product_added', pk)
    return redirect('shop:product_not_found')

def product_added(request, pk):
    if Product.objects.filter(pk=pk).exists():
        context = {'name': Product.objects.get(pk=pk).name,}
        return render(request, 'shop/product_added.html', context)
    else:
        return redirect('shop:product_not_found')

def product_not_found(request):
    return render(request, 'shop/product_not_found.html')

def cart(request):
    cart = []
    for pk in request.session.get('cart', []):
        product = Product.objects.get(pk=pk)
        price = product.price
        name = product.name
        cart.append(f'${price} - {name}')
    context = {'cart': cart}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    if request.method == 'POST':
        request.session['cart'] = []
        return redirect('shop:checkout_successful')
    else:
        cart = request.session.get('cart')
        price = 0
        for pk in cart:
            product = Product.objects.get(pk=pk)
            if product.stock > 0:
                price += product.price
                product.stock -= 1
                product.save()
                if product.stock == 0:
                    product.delete()
            else:
                product.delete()
                return redirect('shop:out_of_stock')
        context = {'price': price}
    return render(request, 'shop/checkout.html', context)

def checkout_successful(request):
    return render(request, 'shop/checkout_successful.html')

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

class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'price', 'stock']
    success_url = reverse_lazy('shop:index')