"""MobileApplicationDec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.shortcuts import render
from .views import brand_view,create_mobile,list_mobiles,mobile_details,user_registeration,user_login,user_logout,order,errorpage,brand_del,brand_update,cart_details,order_del,order_details

urlpatterns = [
    path("error",errorpage,name="errorpage"),
    path("",lambda request:render(request,"mobile/index.html")),
    path("brands",brand_view,name="brandview"),
    path("mobiles",create_mobile,name="createmobile"),
    path("mobiles/list",list_mobiles,name="listmobiles"),
    path("mobiles/details/<int:id>",mobile_details,name="detail"),
    path("mobiles/userregisteration",user_registeration,name="register"),
    path("mobile/userlogin",user_login,name="userlogin"),
    path("mobile/userlogout",user_logout,name="userlogout"),
    path("mobiles/order/<int:id>",order,name='order'),
    path("brands/del/<int:id>",brand_del,name="branddel"),
    path("brands/upd/<int:id>",brand_update,name="brandupdate"),
    path("mobiles/cart",cart_details,name="cart"),
    path("mobiles/cart/delt/<int:id>",order_del,name="orderdel"),
    path("mobiles/cart/view/<int:id>",order_details,name="orderview")
]
