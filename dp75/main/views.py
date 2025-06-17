from django.shortcuts import render

# Create your views here.
def total_price(request):
    return render(request, 'main/total_price.html')