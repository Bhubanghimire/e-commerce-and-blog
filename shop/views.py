from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil 
import datetime
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
    if request.method == 'POST':
        print("bhuban")
        name=request.POST.get('name',"default")
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        address = request.POST.get('country')
        desc=request.POST.get('subject', '')
        print(name,email,phone,address, desc )
        contact = Contact(Name=name, Email= email,Address=address, Phone=phone,Message=desc)
        contact.save()
    return render(request,"shop/contact.html")


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(Order_id=orderId, Email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(Order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')



def search(request):
    return render(request,"shop/search.html")


def checkout(request):
    if request.method == 'POST':
        item_jason = request.POST.get('itemjson',"default")
        name=request.POST.get('name',"default")
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        district = request.POST.get('district')
        address = request.POST.get('address')
        order = Order(Name=name, Email= email, District=district, Address=address, Phone=phone,Item_jason=item_jason)
        order.save()
        Update = OrderUpdate(Order_id=order.Order_id, Update_desc="The order has been placed")
        Update.save()
        thank=True

        id= order.Order_id
        param = {"thank":thank, "id":id}
        print(item_jason)
        return render(request, "shop/checkout.html", param)
       
    return render(request,"shop/checkout.html")


def quickview(request, id):
    prods = Product.objects.get(id=id)
    print(prods)
    param = {"prods":prods}
    return render(request,'shop/detail.html',param)


def productview(request):
    return render(request,"shop/viewproduct.html")