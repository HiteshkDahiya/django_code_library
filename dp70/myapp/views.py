from django.shortcuts import render
from django.contrib import messages
from .models import CartModel


def add_to_cart(request):
    print("Request method:", request.method)
    print("POST data:", request.POST)
    if request.method == "POST":
        if "cart" in request.POST:
            item_name = request.POST["item_name"]
            item_quantity = request.POST["item_quantity"]
            item_price = request.POST["item_price"]
            print(item_name, item_quantity, item_price)
            print('hello django')
            print(f"Received Data - Name: {item_name}, Quantity: {item_quantity}, Price: {item_price}")

            try:
                obj = CartModel.objects.get(item_name=item_name)
                obj.item_quantity = int(obj.item_quantity) + 1
                obj.item_price = int(obj.item_price) + int(item_price)
                obj.save()
                messages.success(request, "Added to Cart!!")
                print("Updated quantity:", obj.item_quantity)

            except CartModel.DoesNotExist:
                item = CartModel.objects.create(item_name=item_name, item_quantity=item_quantity,
                                                item_price=item_price)
                item.save()
                messages.success(request, "Added to Cart!!")

    return render(request,'myapp/index.html')