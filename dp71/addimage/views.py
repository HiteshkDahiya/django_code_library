from django.shortcuts import render
from .models import Product
from django.contrib import messages

def add_product(request):
    print("Request method:", request.method)
    print("POST data:", request.POST)
    if request.method == "POST":
        if "cart" in request.POST:
            name = request.POST.get("name")
            image = request.FILES.get("img")
            # print(name, image)
            print('hello django')
            # print(f"Received Data - Name: {name}, Quantity: {image}")

            item = Product.objects.create(name=name, image=image)
            item.save()
            messages.success(request, "Added to Cart!!")

    return render(request, 'addimage/add_product.html')

def show_product(request):
    products = Product.objects.all()
    return render(request,'addimage/show_product.html',{'products':products})