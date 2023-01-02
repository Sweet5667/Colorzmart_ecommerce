"""colorzproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path("register",views.register,name="register"),
    path("login",views.login_page,name="login"),
    path("logout",views.logout_page,name="logout"),
    path("collection",views.collections,name="collections"),
    path("catagoryview/<str:name>",views.catagoryview,name="collections"),
    path("product_details/<str:cname>/<str:pname>",views.product_details,name="product_details"),
    path("addtocart",views.add_cart,name="addtocart"),
    path("cart",views.cart_view,name="cart"),
    path("remove_cart/<str:pid>",views.remove_cart,name="remove_cart"),
    path("fav",views.fav,name="fav"),
    path("fav_view",views.fav_view,name="fav_view"),
    path("remove_fav/<str:pid>",views.remove_fav,name="remove_fav"),
    path("buy_now",views.buy_now,name="buy_now"),
    path("admin_local",views.admin_local,name="admin_local"),
    path("shipped/<str:pid>",views.shipped,name="shipped"),
    
    
    
    
    
    
]
