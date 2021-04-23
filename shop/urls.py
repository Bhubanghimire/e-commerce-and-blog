from .views import *
from django.urls import path

urlpatterns =[
    path("",home, name="home"),
    path("about/",about, name="aboutshop"),
    path("contact/", contact, name="contactshop"),
    path("tracker/", tracker, name="tracker"),
    path("search/", search, name="searchshop"),
    path("productview/<int:id>",quickview,name="quickview"),
    path("checkout/", checkout, name="checkout"),
]