from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"shop/index.html")

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