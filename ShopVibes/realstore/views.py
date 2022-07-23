from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import product
from .forms import CustomerRegistrationForm, LoginForm
from django.contrib import messages
# Create your views here.
# def home(request):
#     return render(request,'realstore/home.html')

# hello

class ProductView(View):
    
    def get(self,request):
        topwears = product.objects.filter(category ="TW")
        bottomwears = product.objects.filter(category = "BW")
        mobiles = product.objects.filter(category = "M")
        return render(request,'realstore/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles})



def mobile(request,data = None):
    if(data==None):
        mobiles = product.objects.filter(category="M")
    elif (data =='Redmi' or data =='Samsung' or data =='Apple' or data == 'Oppo' ):
        mobiles = product.objects.filter(category="M").filter(brand = data)  
    elif (data == 'below'):
        mobiles = product.objects.filter(category = "M").filter(discounted_price__lt = 10000)    
    elif (data =='above'):
        mobiles = product.objects.filter(category = "M").filter(discounted_price__gt = 10000)      
    return render(request,'realstore/mobile.html',{'mobiles':mobiles})

def profile(request):
    return render(request,'realstore/profile.html')

def orders(request):
    return render(request,'realstore/orders.html')

# def productdetail(request):
    # return render(request,'realstore/productdetail.html')

class productdetailview(View):
    
    def get(self,request,pk):
        unique_product = product.objects.get(pk=pk)
        
        return render(request,'realstore/productdetail.html',{'unique_product':unique_product})




def addtocart(request):
    return render(request,'realstore/addtocart.html')

# def customerregistration(request):
#     return render(request,'realstore/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'realstore/customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congrats! Registered Successfully')
            form.save()
        return render(request,'realstore/customerregistration.html',{'form':form})

# class loginView(View):
    
#     def get(self,request):
#         form = LoginForm()
#         return render(request,'realstore/login.html',{'form':form})

def address(request):
    return render(request,'realstore/address.html')

def checkout(request):
    return render(request,'realstore/checkout.html')

def buynow(request):
    return render(request,'realstore/buynow.html')





