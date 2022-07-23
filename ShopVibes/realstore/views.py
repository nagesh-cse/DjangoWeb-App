from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import cart, customer, product
from .forms import CustomerProfileForm, CustomerRegistrationForm, LoginForm
from django.contrib import messages
# Create your views here.
# def home(request):
#     return render(request,'realstore/home.html')

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
    user=request.user
    product_id=request.GET.get('prod_id')
    Product = product.objects.get(id=product_id)
    cart(user=user, product=Product).save()
    return redirect('/cart')
    

def showcart(request):
    if request.user.is_authenticated:
        user=request.user
        Cart=cart.objects.filter(user=user)
        total_amount=0.0
        amount=0.0
        shipping_amount=50.0
        if Cart:
            for p in Cart:
                if p.user==user:
                    amount=p.product.discounted_price+amount
                    total_amount=amount+shipping_amount
            return render(request, 'realstore/addtocart.html', {'carts': Cart, 'amount': amount, 'total_amount': total_amount, 'shipping_amount': shipping_amount})
        else:
            return render(request, 'realstore/emptycart.html')
        
        
        
        
        
        

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
    address = customer.objects.filter(user = request.user)
    return render(request,'realstore/address.html',{'address':address,'active': 'btn-primary'})

def checkout(request):
    return render(request,'realstore/checkout.html')

def buynow(request):
    return render(request,'realstore/buynow.html')

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()    
        return render(request, 'realstore/profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            data = customer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            data.save()
            messages.success(request, 'Profile Updated Succesfully!')
        return render(request, 'realstore/profile.html', {'form': form, 'active': 'btn-primary'})





