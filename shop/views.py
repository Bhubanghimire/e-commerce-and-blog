from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def home(request):
    all_prods = []
    catprods=Product.objects.values("category")
    cats = {items["category"] for items in catprods}
    
    for cat in cats:
        products = Product.objects.filter(category=cat)
        n = len(products)
        nslide = n//4 + ceil((n/4)-(n//4))
        all_prods.append([products,range(1,nslide),nslide])
    param = {"all_prods":all_prods}
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

def quickview(request, id):
    prods = Product.objects.get(Product_id=id)
    print(prods)
    param = {"prods":prods}
    return render(request,'shop/detail.html',param)

def productview(request):
    return render(request,"shop/viewproduct.html")