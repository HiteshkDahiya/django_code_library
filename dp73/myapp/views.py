from django.shortcuts import render, redirect
from .models import Product
# Create your views here.
def add_image(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.POST['image']
        product = Product.objects.create(name=name,image=image)
        product.save()
        return redirect('/')
    return render(request,'myapp/add.html')


def show_image(request):
    products = Product.objects.all()
    return render(request,'myapp/show.html',{'products':products})

