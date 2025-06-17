from django.shortcuts import render
from .forms import ProductForm
from .models import Product


# add_product view
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    return render(request, 'addimage/add_product.html', {'form': form})

def show_product(request):
    products = Product.objects.all()
    return render(request,'addimage/show_product.html',{'products':products})