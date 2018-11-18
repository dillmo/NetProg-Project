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