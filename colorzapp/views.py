from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from colorzapp.form import CustomUserForm,user_info_form
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json

def home(request):
    catagory=Catagory.objects.filter(status=0)
    products=Product.objects.filter(status=0,trending=1)
    return render(request,'colorzapp/index.html',{"catagory":catagory,"product":products})

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    elif request.method=="POST":
        name=request.POST.get("username")
        pwd=request.POST.get("password")
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged In Successfully..!")
            return redirect("/")
        else:
            messages.error(request,"Invalid User Name Or Password")
            return redirect("/login")
    return render(request,"colorzapp/login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully..!")
    return redirect("/")

def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You  Can Login Now..!")
            return redirect('/login')
    return render(request,"colorzapp/register.html",{"form":form})

def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"colorzapp/collections.html",{"catagory":catagory})

def catagoryview(request,name):
    if(Catagory.objects.filter(status=0,name=name)):
        products=Product.objects.filter(category__name=name)
        return render(request,"colorzapp/products/index.html",{"products":products,"title":name})
    else:
        messages.warning(request,"NO SUCH CATAGORY FOUND")
        return redirect("collections")
    
def product_details(request,cname,pname):
    if(Catagory.objects.filter(status=0,name=cname)):
        catagory=cname
        if(Product.objects.filter(status=0,name=pname)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"colorzapp/products/product_details.html",{"products":products,"catagory":catagory})
        else:
            messages.error(request,"No Such Product Found")
            
def add_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user,product_id=product_id):
                    return JsonResponse({'status':'Product Already In Cart'},status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Added To Cart'},status=200)
                    else:
                        return JsonResponse({'status':'Product Stock Not Available'},status=200)
            
        else:
            return JsonResponse({'status':'Login To Add Cart'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
    
def cart_view(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        if len(cart)>0:
            return render(request,"colorzapp/cart.html",{'cart':cart})
        else:
            messages.warning(request,"Your Cart Is Empty")
            return redirect("/")
            
    else:
        return redirect("/")
    
def remove_cart(request,pid):
    cartitem=Cart.objects.get(id=pid)
    cartitem.delete()   
    return redirect("/cart")

def fav(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Wishlist.objects.filter(user=request.user,product_id=product_id):
                    return JsonResponse({'status':'Product Already In Favourite'},status=200)
                else:
                    Wishlist.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status':'Product Added To Favourite'},status=200)     
        else:
            return JsonResponse({'status':'Login To Add Favourite'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
    
def fav_view(request):
    if request.user.is_authenticated:
        fav=Wishlist.objects.filter(user=request.user)
        if len(fav)>0:
            return render(request,"colorzapp/wishlist.html",{"fav":fav})
        else:
            messages.warning(request,"Your Wishlist Is Empty")
            return redirect("/")
    else:
        messages.warning(request,"Login For View Your Wishlist")
        return(redirect("/"))

def remove_fav(request,pid):
    favitem=Wishlist.objects.get(id=pid)
    favitem.delete()   
    return redirect("/fav_view")

def buy_now(request,id=None):
    form=user_info_form()
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        mobile=request.POST['mobile']
        form=user_info_form(request.POST)
        if form.is_valid():
            print("jvgcfgjmbnvxzsdjgmvncxvzf")
            orders=Cart.objects.filter(user=request.user)
            for i in orders:
                Admin_page.objects.create(user=request.user,product=(i.product),name=name,address=address,mobile=mobile)
                del_from_cart=Cart.objects.get(id=i.id)
                del_from_cart.delete()
            messages.success(request,"Your Order Confirmed ! Thank You !")
            return redirect('/')
    return render(request,"colorzapp/userinfo.html",{"form":form})

def admin_local(request):
    if request.user.is_superuser:
        datas=Admin_page.objects.all()     
        return render(request,"colorzapp/adminview.html",{"datas":datas})
    else:
        return redirect("/")

def shipped(request,pid):
    ship=Admin_page.objects.get(id=pid)
    ship.delete()
    return redirect("/admin_local")
                         
                         
    
    
    
    
    
    
    
    