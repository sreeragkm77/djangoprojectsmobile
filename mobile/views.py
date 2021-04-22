from django.shortcuts import render,redirect
from mobile.forms import BrandCreateForm,MobileCreateForm,OrderForm
from .models import Brands,Mobile,Orders
from .forms import UserRegForm
from django.contrib.auth import authenticate
from  django.contrib.auth import login,logout
# Create your views here.
def admin_permission_updatedelete(func):
    def wrapper(request,id):
        if not request.user.is_superuser:
             return redirect("errorpage")
        else:
            return func(request,id)
    return wrapper
def admin_permission_required(func):
    def wrapper(request):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request)
    return  wrapper
@admin_permission_required
def create_mobile(request):
    form=MobileCreateForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=MobileCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("savrd2")
            return redirect("createmobile")
    return render(request,"mobile/mobilecreate.html",context)
@admin_permission_required
def brand_view(request):
    brands = Brands.objects.all()
    form = BrandCreateForm()
    context = {}
    context["brands"] = brands
    context["form"] = form
    if request.method == 'POST':
        form = BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("brandview")
    return render(request, "mobile/bndcreate.html", context)
@admin_permission_updatedelete
def brand_del(request,id):
    brand=Brands.objects.get(id=id)
    brand.delete()
    return redirect("brandview")
@admin_permission_updatedelete
def brand_update(request,id):
    brand=Brands.objects.get(id=id)
    form=BrandCreateForm(instance=brand)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BrandCreateForm(request.POST,instance=brand)
        if form.is_valid():
            context["form"]=form
            form.save()
        return redirect("brandview")
    return render(request,"mobile/brandupd.html",context)




def errorpage(request):
    return render(request,"mobile/errorpage.html")

def list_mobiles(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobiles.html",context)

def mobile_details(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context["mobile"]=mobile
    return render(request,"mobile/mobiledetail.html",context)
def user_registeration(request):
    form=UserRegForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            form=UserRegForm(request.POST)
            context["form"]=form
            return render(request, "mobile/userreg.html",context)
    return render(request,"mobile/userreg.html",context)
def user_login(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pwd")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("listmobiles")
        else:
            return render(request, "mobile/login.html")

    return render(request,"mobile/login.html")
def user_logout(request):
    logout(request)
    return redirect("userlogin")
def order(request,id):
    product=Mobile.objects.get(id=id)
    username=request.user
    form=OrderForm(initial={'user':username,"product":product})
    context={}
    context['form']=form
    print("getitem")
    if request.method=='POST':
        form = OrderForm(request.POST)
        print("testpoint")
        if form.is_valid():
            form.save()
            return redirect("cart")
        else:
            form = OrderForm(request.POST)
            context["form"] = form
            return render(request, "mobile/orders.html", context)
    return render(request,"mobile/orders.html",context)
def cart_details(request):
    username=request.user
    orders = Orders.objects.filter(user=username)
    print(orders)
    context = {}
    context["orders"] = orders
    return render(request, "mobile/cartdetails.html", context)
def order_del(request,id):
    orders = Orders.objects.get(id=id)
    orders.delete()
    return redirect("cart")
def order_details(request,id):
    mob=Mobile.objects.get(id=id)
    context={}
    context["mob"]=mob
    return render(request,"mobile/orderdetails.html",context)


