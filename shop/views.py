from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def home(request):
    all_products = Product.objects.all()
    print(all_products)
    n=len(all_products)
    nslide = n//4 + ceil((n/4)-(n//4))
    param={"no_of_slide":nslide, 'range':range(1,nslide), "product":all_products}
    return render(request,"shop/home.html",param)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    return render(request,"shop/contact.html")


def tracker(request):
    return render(request,"shop/tracker.html")

def search(request):
    return render(request,"shop/search.html")

def checkout(request):
    return render(request,"shop/checkout.html")

def productview(request):
    return render(request,"shop/viewproduct.html")