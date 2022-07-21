from django.contrib import admin
from .models import customer, orderplaced
from .models import product
from .models import cart
# Register your models here.
# admin.site.register(customer)
@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ('name','locality','zipcode','city','state')
    

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ('title','selling_price','discounted_price','brand','category',)

@admin.register(cart)
class cartAdmin(admin.ModelAdmin):
    list_display = ('user','product','quantity',)  

@admin.register(orderplaced)
class orderplacedAdmin(admin.ModelAdmin):
    list_display = ('user','product','quantity','customer','ordered_date','status',)  