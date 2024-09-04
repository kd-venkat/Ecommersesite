from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    return render(request,"index.html")

def register(request):
    return render(request,"register.html")

def collection(request):
    category = Category.objects.filter(status=0)
    return render(request,"collection.html",{"category":category})


def collectionview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        product =Product.objects.filter(category__name=name)
        return render(request,"collectionview.html",{"product":product,"category_name":name})
    else:
        messages.warning(request ,"No such file")
        return redirect('collection')
    
def productview(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            product = Product.objects.filter(name=pname,status=0).first()
            return render(request,"productview.html",{"product":product})
        else:
            return messages.error(request,"No file")
            return redirect('collection')
    else:   
        return messages.error(request,"No file")
        return redirect("collection")
